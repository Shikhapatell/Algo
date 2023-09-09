
#define a function called is_prime to check if a given number is a prime number or not
def is_prime(num):

  #if the number is less that 2 it will return false 
  if num < 2:
      return False
  #create a variable names counter that is equal to the number minus one 
  counter = num-1

  #using a while loop to iterate each time the counter variable is greater then one
  while(counter > 1):
    # if the number is divisible by a factor, it is not prime and return false
    if num % counter == 0:
      return False
    #each iteration counter is subtracted by one 
    counter -= 1

  #otherwise return true 
  return True

#define a function called count_primes to count the number of primes in a list
def count_primes(list_with_primes):

    #start with a constant varibale prime that is equal to 0
    primes = 0

    #for each number in the list if the item is prime it will increase the count of primes 
    for x in list_with_primes:
        if(is_prime(x)):
            primes += 1
    #return the total number of prines in the list
    return primes

#define a function called bubble_sort to sort the given list using bubble sort algorithm
def bubble_sort(sorting_list):
  #get the length of the list
  n = len(sorting_list)
  #loop through all possible pairs of adjacent numbers in the list
  for i in range(n-1):
    for j in range(0, n-i-1):
      #if the first number is greater than the second number, swap them
      if sorting_list[j] > sorting_list[j + 1] :
        sorting_list[j], sorting_list[j + 1] = sorting_list[j + 1], sorting_list[j]

#define a function called get_average that calculates the average of a list of numbers
def get_average(list_to_average):
  #set a variable for the total sum of the numbers to 0
  total = 0
  #loop through all numbers in the list
  for i in list_to_average:
    #add each number to the total sum
    total = total + i
  #divide the total sum by the number of numbers to get the average and return that value
  return round(total/len(list_to_average))

#define the main function that runs the program
def main():
  #create an empty list to store the user's input
  user_list = []
  #prompt the user to enter a number
  user_num = input('Enter a number (type "Done" when finsished): ')
  #loop through input until the user is done
  while(user_num.lower() != 'done'):
    try:
      #try to convert the input to an integer and append it to the list
      user_num = int(user_num)
      user_list.append(user_num)
    except ValueError as err:
      #if the input is not an integer, print an error message
      print(err,'That was not a number!')
    #prompt the user to enter another number or type "Done"
    user_num = input('Enter another number (type "Done" when finsished): ')

  #print the user's list of numbers
  print('Your list:',user_list)
  #print the number of primes in the user's list
  print('Your list has',count_primes(user_list),'primes')
  #print the average of the user's list of numbers
  print('Average:',get_average(user_list))
  #sort the user's list of numbers using bubble sort
  bubble_sort(user_list)
  #print the sorted list of numbers
  print('Your list sorted:',user_list)
  

#check if this is the main module
if __name__=="__main__":
  #run the main function (which should always run first)
  main()
