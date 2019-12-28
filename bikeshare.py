import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Please enter name of the city to analyze: ').lower()
            if city not in ('chicago', 'new york city', 'washington'):
                print('Please choose chicago, new york city or washington')
            else:
                break
        except:
            print('Please choose chicago, new york city or washington')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Please enter name of the month to filter by, or "all" to apply no month filter: ').lower()
            if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
                print('Please choose a valid month')
            else:
                break
        except:
            print('Please choose a valid month')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Please enter name of the day of week to filter by, or "all" to apply no day filter: ').lower()
            if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                print('Please choose a valid weekday name')
            else:
                break
        except:
            print('Please Enter a valid weekday name')
            continue

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    while True:
        try:
            stats = input('\nWould you like to view statistics on the most frequent times of travel?\nEnter yes or no.\n').lower()
            if stats not in ('yes', 'no'):
                print('Please Enter yes or no')
            else:
                break
        except:
            print('Please Enter yes or no')
            continue
        
    if stats == 'yes':
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # TO DO: display the most common month
        mcm = df['month'].mode()[0]
        print('Most common month is ', mcm)

        # TO DO: display the most common day of week

        mcd = df['day_of_week'].mode()[0]
        print('Most common day is ', mcd)

        # TO DO: display the most common start hour
        df['hour'] = df['Start Time'].dt.hour
        mch = df['hour'].mode()[0]
        print('Most common start hour is ', mch)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print('Skipping statistics on the most frequent times of travel.')

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    while True:
        try:
            stats = input('\nWould you like to view statistics on the most popular stations and trip?\nEnter yes or no.\n').lower()
            if stats not in ('yes', 'no'):
                print('Please Enter yes or no')
            else:
                break
        except:
            print('Please Enter yes or no')
            continue
    if stats == 'yes':
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO: display most commonly used start station
        mcss = df['Start Station'].value_counts().idxmax()
        print('Most commonly used start station is ', mcss)


        # TO DO: display most commonly used end station
        mces = df['End Station'].value_counts().idxmax()
        print('Most commonly used end station is', mces)

        # TO DO: display most frequent combination of start station and end station trip
        combo_station = df.groupby(['Start Station', 'End Station']).count()
        print('The most frequent combination of start station and end station trip ', mcss, ' & ', mces, ' => ', combo_station)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print('Skipping statistics on the most popular stations and trip.')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    while True:
        try:
            
            stats = input('\nWould you like to view statistics on the total and average trip duration?\nEnter yes or no.\n').lower()
            if stats not in ('yes', 'no'):
                print('Please Enter yes or no')
            else:
                break
        except:
                print('Please Enter yes or no')
                continue
    if stats == 'yes':

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        ttt = sum(df['Trip Duration'])
        print('Total travel time is ', ttt/86400, " d")

        # TO DO: display mean travel time
        mtt = df['Trip Duration'].mean()
        print('Mean travel time is ', mtt/60, " m")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print('Skipping statistics on the total and average trip duration.')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types\n', user_types)


    # TO DO: Display counts of gender
    try:
        gt = df['Gender'].value_counts()
        print('Gender count\n ', gt)

    except KeyError:
        print('Gender count Could not find data')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      ey = df['Birth Year'].min()
      print('Earliest year of birth is ', ey)

    except KeyError:
      print("Could not find data")

    try:
      mry = df['Birth Year'].max()
      print('Most recent year of birth is ', mry)

    except KeyError:
      print('Could not find data')

    try:
      mcy = df['Birth Year'].value_counts().idxmax()
      print('Most common year of birth is  ', mcy)

    except KeyError:
      print('Could not find data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        while True:
            try:
                view_rd = input('\nWould you like to view first five raw data?\nEnter yes or no.\n').lower()
                if view_rd not in ('yes', 'no'):
                    print('Please Enter yes or no')
                else:
                    break
            except:
                print('Please Enter yes or no')
                continue
        x = 0
        while view_rd == 'yes':
            y = x + 5
            vrd = df[x:y]
            print(vrd)
            x += 5
            while True:
                try:
                    view_rd = input('\nWould you like to view next five raw data?\nEnter yes or no.\n').lower()
                    if view_rd not in ('yes', 'no'):
                        print('Please Enter yes or no')
                    else:
                        break
                except:
                    print('Please Enter yes or no')
                    continue

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
