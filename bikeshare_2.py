import time
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 500)
#import datetime        #only needed if datetime.timedelta is used as an alternative solution, here a self-written function is used instead.

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        city=input('\nPlease enter the city of interest, chicago, new york city, or washington:\n').lower()

        while city not in ['chicago','new york city','washington'] :
            print('Sorry... it seems like you\'re not typing a correct entry.')
            print('Let\'s try again!')
            city=input('\nPlease enter the city of interest, chicago, new york city, or washington:\n').lower()

        print('Great! the chosen entry is: {}\n'.format(city))

    except:
        print('Seems like there is an issue with your input')

    # city=None
    # while city not in ['chicago','new york city','washington']:
    #     city=input('\nPlease enter the city of interest, chicago, new york city, or washington:').lower()

    # get user input for month (all, january, february, ... , june)

    try:
        month=input('\nPlease enter the month of interest from January to June, eg. january, february,..., or all?:\n').lower()

        while month not in ['january','february','march','april','may','june','all'] :
            print('Sorry... it seems like you\'re not typing a valid entry.')
            print('Let\'s try again!')
            month=input('\nPlease enter the month of interest from January to June, eg. january, february,..., or all?:\n').lower()

        print('Great! the chosen entry is: {}\n'.format(month))

    except:
        print('Seems like there is an issue with your input')

    # month=None
    # while month not in ['january','february','march','april','may','june','all']:
    # #while month not in ['january','february','march','april','may','june']:
    #     month=input('\nPlease enter the month of interest from January to June, eg. january, february,..., or all?:').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    try:
        day=input('\nPlease enter day of week of interest, eg. monday, tuesday,..., or all?:\n').lower()

        while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'] :
            print('Sorry... it seems like your entry is not valid.')
            print('Let\'s give it another try!')
            day=input('\nPlease enter day of week of interest, eg. monday, tuesday,..., or all?:\n').lower()

        print('Great! the chosen entry is: {}\n'.format(day))

    except:
        print('Seems like there is an issue with your input')
    # day=None
    # while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
    #     day=input('\nPlease enter day of week of interest, eg. monday, tuesday,..., or all?:').lower()

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
    df = pd.read_csv('./'+CITY_DATA[city])

        # convert the Start Time column to datetime, please refer to [1] in readme.txt.
    df['Start Time'] = pd.to_datetime(df['Start Time'],format="%Y-%m-%d %H:%M:%S")

        # extract month and day of week from Start Time to create new columns, please reder to [2] in readme.txt
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    #print(df['Start Time'])    #to print the intermitant output
    #print(df['month'])         #to print the intermitant output
    #print(df['day_of_week'])   #to print the intermitant output

    if month != 'all':
            # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1    #refer to [3] in readme.txt

            # filter by month to create the new dataframe
        df = df.loc[df['month']==month]

            # filter by day of week if applicable
    if day != 'all':
            # filter by day of week to create the new dataframe
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = days.index(day)           #refer to [3] in readme.txt
        df = df.loc[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month=df['month'].value_counts().idxmax()       #refer to [4] in readme.txt
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('The most common month is {}. '.format(months[popular_month-1].title()))

    # display the most common day of week
    popular_day=df['day_of_week'].value_counts().idxmax()   #refer to [4] in readme.txt
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    print('The most common day of week is {}. '.format(days[popular_day].title()))

    # display the most common start hour
    #df['Start Time'] =pd.to_datetime(df['Start Time'],format="%Y-%m-%d %H:%M:%S")  #to convert the data into date format
    # extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour                #refer to [2] in readme.txt
    popular_hour=df['hour'].value_counts().idxmax()     #refer to [4] in readme.txt
    print('The most common start hour is {}:00. '.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    #df['Start Station']=df['Start Station'].dropna(axis=0)  # This is not needed as value_counts() already takes into account of NaN
    popular_start_station=df['Start Station'].value_counts().idxmax()   #refer to [4] in readme.txt
    print('The most popular start station is: ',popular_start_station)

    # display most commonly used end station
    #df['End Station']=df['End Station'].dropna(axis=0)  # This is not needed as value_counts() already takes into account of NaN
    popular_end_station=df['End Station'].value_counts().idxmax()   #refer to [4] in readme.txt
    print('The most popular end station is: ',popular_end_station)

    # display most frequent combination of start station and end station trip
    #popular_start_end_station=df.value_counts(['Start Station','End Station']).idxmax()     #refer to [5] in readme.txt, this is supported from pandas version > 1.1
    #print('The most popular combination of start station and end station trip is: ',popular_start_end_station)
    popular_start_end_station=df.groupby(['Start Station','End Station']).count().idxmax()
    #popular_start_end_station=df.groupby(['Start Station','End Station']).count().idxmax() #idxmax() #This is an alternative way if panda version is < 1.1.
    print('The most popular combination of start station and end station trip is: ',popular_start_end_station[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_tt=df['Trip Duration'].sum()
    # a self-built function secondstoDHMS(time) is used here, please refer to [6] in readme.txt
    print('The total travel time is {} day(s) {} hour(s) {} minute(s) {} seconds. '.format(secondstoDHMS(total_tt)[0],secondstoDHMS(total_tt)[1],secondstoDHMS(total_tt)[2],secondstoDHMS(total_tt)[3]))

    # display mean travel time
    mean_tt=df['Trip Duration'].mean()
    # a self-built function secondstoDHMS(time) is used here, please refer to [6] in readme.txt
    print('The mean travel time is {} day(s) {} hour(s) {} minute(s) {} seconds. '.format(secondstoDHMS(mean_tt)[0],secondstoDHMS(mean_tt)[1],secondstoDHMS(mean_tt)[2],secondstoDHMS(mean_tt)[3]))

    #print('The mean travel time in HH:MM:SS is: ',str(datetime.timedelta(seconds=mean_tt)))  #alternative solution, refer to [7] in readme.txt

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def secondstoDHMS(time):
    """This is added to convert seconds to days, hours, minutes and seconds, refer to [6] in readme.txt"""
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = round(time,2)
    return int(day), int(hour), int(minutes), seconds

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print('The counts of each user type are given below: \n')
    print(user_types.to_string(header=False))                   #to remove header and footnote of output, refer to [8] in readme.txt


    # Display counts of gender
    #if df.get('Gender')==None:                 #didn't work in some cases.
    if 'Gender' not in df.columns:              #to check if a column exists, refer to [9] in readme.txt
        print('Sorry, there is no data about Gender is available!')
    else:
        gender = df['Gender'].value_counts()

        print('The counts of each gender group are given below: \n')
        print(gender.to_string(header=False))           #to remove header and footnote of output, refer to [8] in readme.txt

    # Display earliest, most recent, and most common year of birth
    #if df.get('Birth Year')==None:             #didn't work in some cases.
    if 'Birth Year' not in df.columns:          #to check if a column exists, refer to [9] in readme.txt
        print('Sorry, there is no data about Birth Year is available!')
    else:
        min_birthy=df['Birth Year'].min()
        max_birthy=df['Birth Year'].max()
        common_birthy=df['Birth Year'].value_counts().idxmax()  #refer to [4] & [4a] in readme.txt to determine index of max. count
        print('The earliest year of birth among the users is {}. \n'.format(int(min_birthy)))
        print('The most recent year of birth among the users is {}. \n'.format(int(max_birthy)))
        print('The most common year of birth among the users is {}. \n'.format(int(common_birthy)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """This function is to display data as long as the users enter yes"""
    view_data=None
    while view_data not in ['yes','no']:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        start_loc = 0
        while (view_data=='yes'):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data=None
            while view_data not in ['yes','no']:
                view_data = input("\nDo you wish to continue? Enter yes or no: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
