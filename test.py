from datetime import datetime

from calcular_siguiente_asamblea import properes_numero, next_activity_from_date, Activity, \
    find_start_date_from_activity, get_activities_between_dates

import unittest

class TestActivityFunctions(unittest.TestCase):

    def test_get_correct_start_date_from_date_we_want_to_be_the_next(self):
        # Given a date, we want to find the start date that will make the next activity the one we want
        # activity = Activity(("18:00", "💥Thai"), datetime(2024, 4, 10))
        date = datetime(2024, 5, 27, 18, 0)
        activity = Activity(("18:00", "💥Thai"), date)
        result = find_start_date_from_activity(activity)
        next = next_activity_from_date(datetime.now(), start_date=result)
        self.assertEqual(next.date, date)  # Ensure we get the correct start date

    def test_get_next_activities_from_today(self):
        # Test the next X activities from today
        result = properes_numero(11)
        self.assertEqual(len(result), 11)  # Ensure we get 10 activities
        msg = ""
        for activity in result:
            msg += "🌟" + activity.telegram_repr + "\n"
        print(msg)

    def tets_next_activity_from_date(self):
        # Calcular next from today
        print(next_activity_from_date(datetime.now()))
        print(next_activity_from_date(datetime(2024, 4, 10, 18, 0)))

    def test_get_activities_between_dates(self):
        # Calculate activity from origin to date
        activity_dates = get_activities_between_dates(datetime(2024, 10, 22))
        print("From now to endate", )
        for activity in activity_dates:
           print(activity)




if __name__ == '__main__':
    unittest.main()

#
#
# def test():
#     msg = ""
#     # Find origin to fetch certain activity/date
#     # activity = Activity(("18:00", "💥Thai"), datetime(2024, 4, 10))
#     # activity = Activity(("18:00", "💥Thai"), datetime(2024, 5, 27))
#     # print(find_start_date_from_activity(activity))
#
#     # Calcular next from today
#     print(next_activity_from_date(datetime.now()))
#     print(next_activity_from_date(datetime(2024, 4, 10, 18, 0)))
#
#     # # Calcular properes
#     for activity in properes_numero(10):
#         # format the message
#         msg += "🌟" + activity.telegram_repr + "\n"
#     print(msg)
#
#     # Example usage
#     # end_date = "2024-01-27"
#     # end_date = datetime.strptime(end_date, '%Y-%m-%d')
#
#     # # Calculate next activity
#     # activity_dates = next_activity_from_date(end_date)
#     # print("Next activity", activity_dates)
#
#     # Calculate activity from origin to date
#     # activity_dates = get_activities_between_dates(datetime(2024, 10, 22))
#     # print("From now to endate", )
#     # for activity in activity_dates:
#     #    print(activity)
#
#     # Calculate activity by month
#     # year = 2024
#     # month = 2
#     # print("For month", year, month)
#
#     # Calculate activity dates for the specified month
#     # activity_dates_month = get_activites_of_a_month(year, month)
#     # for activity in activity_dates_month:
#     #     print(activity)
#
# test()
