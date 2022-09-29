def main(number):

    answer = 0

    answer += number % 10
    number //= 10
    
    answer += number % 10
    number //= 10

    answer += number % 10
    number //= 10
    
    answer += number % 10
    number //= 10

    return answer

print(main(7777))

def main(number):

    answer = 0

    answer += number % 10 % 2
    number  //= 10

    answer += number % 10 % 2
    number  //= 10

    answer += number % 10 % 2
    number  //= 10

    answer += number % 10 % 2

    return answer

print(main(9879))

def main(number):

    counter = 0

    x1 = number % 10 + 1
    counter += x1 % 2
    number //= 10

    x2 = number % 10 + 1
    counter += x2 % 2
    number //= 10
    
    x3 = number % 10 + 1
    counter += x3 % 2
    number //= 10

    x4 = number % 10 + 1
    counter += x4 % 2
    number //= 10

    return counter

print(main(8888))

def main(number):

    sum_odd = 0

    x1 = number % 10
    sum_odd += x1 % 2 * x1
    number //= 10

    x2 = number % 10
    sum_odd += x2 % 2 * x2
    number //= 10

    x3 = number % 10
    sum_odd += x3 % 2 * x3
    number //= 10

    x4 = number % 10
    sum_odd += x4 % 2 * x4
    number //= 10

    return sum_odd

print(main(7485))

def main(number):

    sum_even = 0

    x1 = number % 10
    sum_even += (x1 + 1) % 2 * x1
    number //= 10

    x1 = number % 10
    sum_even += (x1 + 1) % 2 * x1
    number //= 10

    x1 = number % 10
    sum_even += (x1 + 1) % 2 * x1
    number //= 10

    x1 = number % 10
    sum_even += (x1 + 1) % 2 * x1
    number //= 10

    return sum_even

print(main(4874))