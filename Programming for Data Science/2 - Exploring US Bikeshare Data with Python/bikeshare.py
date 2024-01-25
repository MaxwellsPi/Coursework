import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city_dict):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    i=True
    while i == True :
        city = input('Please enter a city (chicago,new york or washington):')
        city = str.lower(city)
        
        if city in list(city_dict.keys()):
            break
        else:
            print('Please enter a valid city.')
            
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = list(map(lambda x: x.lower(), list(filter(None,calendar.month_name))))
    while i == True :
        month = input('Please enter a month (all, january, february, ... , june):')
        month = str.lower(month)

        if month in list(month_list) or month == 'all':
            break
        else:
            print('Please enter a valid month.')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = list(map(lambda x: x.lower(), list(filter(None,calendar.day_name))))
    while i == True :
        day = input('Please enter a day (all, monday, tuesday, ... , sunday):')
        day = str.lower(day)

        if day in list(day_list) or day == 'all':
            break
        else:
            print('Please enter a valid day.')
            
            

    print('-'*40)
    return city, month, day


def load_data(city, month, day, city_data):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    file_name = city_data[city] 
    raw_data = pd.read_csv(file_name)
    df = raw_data.copy()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    month_list = list(map(lambda x: x.lower(), list(filter(None,calendar.month_name))))
    month = month_list.index('january') + 1

    if month != 'all':
        df = df[df['Start Time'].dt.month == month]
    
    if day != 'all':
        df = df[df['Start Time'].dt.day_name() == day.title()]
        
    df.dropna(axis=0,inplace=True)
    
    return raw_data, df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month: {}'.format(df['Start Time'].dt.month.mode()[0]))

    # TO DO: display the most common day of week
    print('Most common day of the week: {}'.format(df['Start Time'].dt.day_name().mode()[0]))

    # TO DO: display the most common start hour
    print('Most common start hour: {}'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('Most commonly used end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start and end station: {} and {}'.format(
        df.groupby(['Start Station','End Station']).size().idxmax()[0], 
        df.groupby(['Start Station','End Station']).size().idxmax()[1]
    ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean travel time: {}'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        print('Counts of user type:')
        
        for user_type in df['User Type'].unique():
            print(user_type + ':' + str(df['User Type'].value_counts()[user_type]))
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of gender:')
        print(df['Gender'].value_counts().index[0] + ':' + str(df['Gender'].value_counts()[0]))
        print(df['Gender'].value_counts().index[1] + ':' + str(df['Gender'].value_counts()[1]))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Ealiest year of birth: {}'.format(int(df['Birth Year'].min())))
        print('Most recent year of birth: {}'.format(int(df['Birth Year'].max())))
        print('Most common year of birth: {}'.format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def print_raw_data(df):
    """Prompts user to print 5 rows of raw data"""
    
    def check_response(response):
        response = response.lower()
        
        i=True
        while i==True:
            if response in ['yes','no']:
                break
            else:
                print('Please enter a valid response.\n')
                response = input('Would like to see the raw data (yes,no)?')

        return response

    
    response = input('Would like to see the raw data (yes,no)?')
    response = check_response(response)
    
    
    i=0
    while response=='yes':
        print(df[i:i+5])
        
        response = input('Would like to see the next five lines (yes,no)?')
        response = check_response(response)
        
        if response == 'yes':
            None
        else:
            break
        
        i+=5
        if i > len(df):
            print(df[i:])
        else:
            None
             

def main(city_df):
    while True:
        city, month, day = get_filters(city_df)
        raw_data, df = load_data(city, month, day, city_df)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        print_raw_data(raw_data)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main(CITY_DATA)