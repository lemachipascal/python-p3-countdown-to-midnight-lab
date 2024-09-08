# your code goes here!
def countdown(start):
    while start > 0:
        print(f'{start} SECOND(S)!')
        start -= 1
    print('HAPPY NEW YEAR!')

print(countdown(10))

import time

def countdown_with_sleep(start):
    while start > 0:
        print(f'{start} SECOND(S)!')
        time.sleep(1)  # Sleep for 1 second
        start -= 1
    print('HAPPY NEW YEAR!')
print(countdown_with_sleep(10))