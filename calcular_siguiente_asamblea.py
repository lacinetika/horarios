import json
from datetime import datetime, timedelta
from calendar import monthrange
from typing import Callable

import settings
from utils.remove_emojis import remove_emojis
from settings import START_DATE, SCHEDULES

settings_start_date = datetime.strptime(START_DATE, '%Y-%m-%d')
json_data = SCHEDULES
day_names = ["monday", "tuesday", "wednesday", "thursday", "friday"]


class Activity:
    def __init__(self, activity, date: datetime):
        self.time = activity[0]
        self.name = activity[1]
        self.date = date
        # Add the time to the date
        self.date = datetime.combine(date, datetime.strptime(self.time, '%H:%M').time())

    def __str__(self):
        day = self.date.strftime('%A').lower()
        return f"{day} {self.date.strftime('%Y-%m-%d')} {self.time} {self.name}"

    # Property of the activity representation to send on a telegram message
    @property
    def telegram_repr(self):
        return f"{self.date.strftime('%A, *%d* de *%B* a las *%H:%M*')} en horari de  *{self.name}*"

    # Send the activity text on a format to be written on the image
    @property
    def img_repr(self):
        return f"{self.date.strftime('%d de %B a las %H:%M')}\nen horari de {remove_emojis(self.name)}"





def parse_schedule(json_data):
    json_schedule = json.loads(json_data)
    for day in json_schedule:
        json_schedule[day] = sorted(json_schedule[day].items())
    return json_schedule


schedule = parse_schedule(json_data)


def _find_next_activity_of_day(times, last_time):
    # Find the next time slot
    next_activity_time = None
    for time in sorted(times):
        if time > last_time:
            next_activity_time = time
            break

    if next_activity_time:
        return next_activity_time, times[next_activity_time]
    else:
        next_activity_time = sorted(times.keys())[0]
        return next_activity_time, times[next_activity_time]


def _calculate_next_date(end_date: datetime,
                         cb: Callable[[Activity], None] = None,
                         start_date=settings_start_date):
    # Current date for iteration, starting with the start date
    current_date = start_date
    last_activity = {day: None for day in schedule.keys()}  # Track the last activity for each day

    while True:
        # Calculate the next activity date
        if current_date.weekday() == 4:  # Friday
            current_date += timedelta(days=10)
        else:
            current_date += timedelta(weeks=2, days=1)
        day = current_date.strftime('%A').lower()
        if last_activity[day] is not None and len(schedule[day]) > 1:
            # get the times of the schedule from the dict object
            times_of_day = {time: activity for time, activity in schedule[day]}
            next_schedule = _find_next_activity_of_day(times_of_day, last_activity[day].time)
            current_activity = Activity(next_schedule, current_date)
        else:
            current_activity = Activity(schedule[day][0], current_date)
        if cb is not None:
            cb(current_activity)
        last_activity[day] = current_activity
        if current_date > end_date:
            break
    return current_activity


def next_activity_from_date(today_date: datetime, use_count_from=True, start_date=settings_start_date):
    """
    Calculate the next activity by a given day.
    :param use_count_from: if true, will check the COUNT_FROM setting
    :param today_date:
    :return:
    """
    # Used to show activites from a specific date
    if use_count_from and settings.COUNT_FROM:
        new_today_date = datetime.strptime(settings.COUNT_FROM, '%Y-%m-%d')
        if new_today_date > today_date:
            today_date = new_today_date
    activity = _calculate_next_date(today_date, start_date=start_date)
    return activity


def get_activities_between_dates(end_date: datetime) -> list[Activity]:
    # List to store all activity dates
    activities = []
    _calculate_next_date(end_date, lambda a: activities.append(a))
    return activities


def get_activites_of_a_month(year: int, month: int):
    # Convert start and end dates to datetime objects
    last_day = monthrange(year, month)[1]
    end_date = datetime(year, month, last_day)
    # List to store activity dates for the specific month
    activities = []
    def save_date(activity: Activity):
        if activity.date.year == year and activity.date.month == month:
            activities.append(activity)
    _calculate_next_date(end_date, save_date)
    return activities


def properes_numero(number, start_date=settings_start_date):
    today = datetime.now()
    # loop to get the next 3 months activites on an array of activities
    activities = []
    next = None
    for i in range(number):
        if(next is not None):
            today = next.date
        next = next_activity_from_date(today, start_date=start_date)
        activities.append(next)
    return activities # Flat activities array


def find_start_date_from_activity(activity: Activity):
    start_date = datetime(2023, 10, 2)
    today = activity.date + timedelta(days=-1) # Use the day before to the activity day you want to find
    current_date = start_date
    for i in range(365):
        try:
            candidate = next_activity_from_date(today_date=today, use_count_from=False, start_date=current_date)
            print(i, "candidate", candidate, current_date)
            if candidate.date == activity.date and \
                    candidate.name == activity.name and candidate.time == activity.time:
                return current_date
        except KeyError:
            print(KeyError)
        current_date += timedelta(days=1)


