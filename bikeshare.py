import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_D=['chicago','new york city','washington']
month_D= ['all','january','february','march','april','may','june']
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
    
    city=input(" enter the city :").lower() 
    while  city not in city_D:
        print("city is not correct")
        city = input ("CHOOSE BETWEEN chicago, new york city OR washington: ")
        

    # TO DO: get user input for month (all, january, february, ... ,city = input ("CHOOSE BETWEEN chicago, new york city OR washington: ") june)
    month=input(" enter the month :").lower() 
    while  month not in month_D:
        print("month is not correct")
        city = input ("ENTER MONTH january, february, ... , june :")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_D= ['all','sunday','monday','tuesday','wensday','thursday','friday','sutarday']
    while True:
        day=input(" enter the day :").lower() 
        if day in day_D:
            break
        else:
            print("day is not correct")
        #day = input ("choose between sunday, monday, ... , sutarday :")

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
    df['hour'] = df['Start Time'].dt.hour

  
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]

    
    if day != 'all':
       
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(" This is the most common month : ",df['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print(" This is the most common day of week : ",df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print(" This is the most common start hour : ",df['hour'].value_counts().idxmax())
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: ", df ['Start Station'].value_counts().mode()[0])

    # TO DO: display most commonly used end station
    print("The most common end station is: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    df[' trip']= df['Start Station']+ 'to' + df['End Station']
    print(format(df[' trip'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum() / 3600.0
    print("total travel time in hours is: ", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean() / 3600.0
    print("mean travel time in hours is: ", mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city_D):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    if city_D != 'washington':
        # TO DO: Display counts of gender
        user_gender = df['Gender'].value_counts()
        print(user_gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yearOfBirth = int(df['Birth Year'].min())
        most_recent_yearOfBirth = int(df['Birth Year'].max())
        most_common_yearOfBirth = int(df['Birth Year'].value_counts().idxmax())
        print("The earliest year of birth is:",earliest_yearOfBirth,
              ", most recent one is:",most_recent_yearOfBirth,
              "and the most common one is: ",most_common_yearOfBirth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def show_row_data(df):
    row=0
    while True:
        view_raw_data = input("Would you like to see the raw data? for 'Yes' enter 'Y' and for 'No' enter 'N'.\n").lower()
     
        if view_raw_data == "y":
            print(df.iloc[row : row + 5])
            row += 5
        elif view_raw_data == "n":
            break
        else: #validate user input
            print("Sorry! You entered Wrong Input, try Again!")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city_D)
        show_row_data(df)
        restart = input('\nWould you like to restart? Enter "y" for yes or "n" for no.\n').lower()
        if restart.lower() != 'y':
            break    



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
