import time
import pandas as pd



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington).


    while True:
        city = input('Which of the following cities would like to explore? Please choose from Chicago, New York City or Washington ')

        city = city.lower()
        print('your input:', city)

        if city not in ('new york city','chicago','washington'):
            print('Sorry, please select one of the cities: Chicago, New York City or Washington ')
            print('invalid input:', city)
            continue
        else:
            break

    # Get user input for month (all, january, february, ... , june).
    while True:
      month = input("Which month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference? ")
      month = month.lower()
                     
      if month not in ('january','february','march','april','may','june','all'):
        print('Sorry, please try again.')
        continue
      else:
        break

    # Get user input for day of week (all, monday, tuesday, ... sunday).
    while True:
        day = input('which day of the week would you like to explore? Choose a day or enter all ')

        day = day.lower()
        

        if day not in ('monday','tuesday','wednesday','thursday','friday','all'):
            print('Sorry, try again!')
            continue
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day) 
        df = df[df['Weekday'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month.
    
    popular_month = df['Month'].mode()[0]
    
    if popular_month == 1:
        popular_month = "January"
    elif popular_month == 2:
        popular_month = "February"
    elif popular_month == 3:
        popular_month = "March"
    elif popular_month == 4:
        popular_month = "April"
    elif popular_month == 5:
        popular_month = "May"
    elif popular_month == 6:
        popular_month = "June"
    print('Most Common Month: \n', popular_month)


    # Display the most common day of week.
    popular_day = df['Weekday'].mode()[0]
    print('Most Common Day of the Week: \n', popular_day) 



    # Display the most common start hour.
    df['Hour'] = df['Start Time'].dt.hour #PB
    popular_hour = df['Hour'].mode()[0] #PB
    if popular_hour < 12:
        print('Most Common Start Hour:', popular_hour, ' AM')
    elif popular_hour >= 12:
        if popular_hour > 12:
            popular_hour -= 12
        print('Most Common Start Hour:', popular_hour, ' PM')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station: \n", popular_start_station)
    
    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most Common End Station: \n", popular_end_station)
    
    # Display most frequent combination of start station and end station trip
    combo_station = df['Start Station'] + " to " +  df['End Station']
    common_combo_station = combo_station.mode()[0]
    print("Most Common Trip from Start to End:\n {}".format(common_combo_station)) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time.
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print("The Total Travel Time is {} Hours, {} Minutes, and {} Seconds.".format(hour, minute, second))



    # Display mean travel time.
    average_duration = round(df['Trip Duration'].mean())
    minute, second = divmod(average_duration, 60)
    if minute> 60:
        hour, minute = divmod(minute, 60)
        print('The Average Travel Time is {} Hours, {} Minutes, and {} seconds.'.format(hour, minute, second))
    else:
        print('The Average Trip Duration is {} Minutes and {} Seconds.'.format(minute, second))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types.
    user_types = df['User Type'].value_counts()
    print("Counts of Each User Type:\n", user_types)


    # Display counts of gender.
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    # Display earliest, most recent, and most common year of birth.
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details in this file.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def raw_data (df):
    
    print('press enter to see raw data, press no to skip')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
