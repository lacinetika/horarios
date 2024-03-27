from datetime import datetime

from calcular_siguiente_asamblea import properes_numero, next_activity_from_date, Activity, \
    find_start_date_from_activity


def test():
    msg = ""
    activity = Activity(("18:00", "💥Thai"), datetime(2024, 4, 10))
    print(find_start_date_from_activity(activity))

    # Calcular next from today
    print(next_activity_from_date(datetime.now()))
    #
    # # Calcular properes
    # for activity in properes_numero(4):
    #     # format the message
    #     msg += "🌟" + activity.telegram_repr + "\n"
    # print(msg)


    # Example usage
    # end_date = "2024-01-27"
    # end_date = datetime.strptime(end_date, '%Y-%m-%d')
    # # Calculate next activity
    # activity_dates = next_activity_from_date(end_date)
    # print("Next activity", activity_dates)
    # # Calculate activity dates
    # activity_dates = get_activities_between_dates(datetime(2024, 10, 22))
    # print("From now to endate", )
    # for activity in activity_dates:
    #    print(activity)
    # # Calculate activity by month
    # year = 2024
    # month = 2
    # print("For month", year, month)
    # # Calculate activity dates for the specified month
    # activity_dates_month = get_activites_of_a_month(year, month)
    # for activity in activity_dates_month:
    #     print(activity)

test()
