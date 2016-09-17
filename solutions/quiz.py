import doctest
import re
import collections

# quiz 1
print("Hello CodingGrils!")

# quiz 2
q = "CodingGirls"
print(q[-1::] == "s")
print(q[:-1:] == "CodingGirl")
print(q[::-1] == "slriGgnidoC")

# quiz 3
print("-42".zfill(5))
print(
    "D Hello world! "
    .strip("! ")
    .lstrip("D ")
    .title()
)

# quiz 4
print("03-30-2016".split("-"))

# quiz 5
word = input("Please enter a word: ")
if word:
    reversed_word = word[::-1]
    if word == reversed_word:
        print(
            "Hooray! {} is a palindrome."
            .format(word)
        )
    else:
        print(
            "Sad leh! {} is not a palindrome."
            .format(word)
        )
else:
    print("word length smaller than 1.")

# quiz 6
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_primes(n):
        '''get_primes

        A function return a list of prime numbers smaller than n

        Args:
            n: end point (int)

        Return:
            prime numbers smaller than n (list)

        >>> get_primes(13)
        [2, 3, 5, 7, 11]

        '''
        # return [number for number in range(2, n)
        #    if is_prime(number)]
        result_list = []
        for num in range(2, n):
            if (is_prime(num)):
                result_list.append(num)
        return result_list

doctest.run_docstring_examples(get_primes, globals())
print(get_primes(8))

# quiz 7
def is_phone(phone):
    '''is_phone

    A function check if phone is a valid phone number
    Hint: \d captures [0-9]

    Args:
        phone: phone number to check (str)

    Return:
        True if phone is valid, False otherwise (bool)

    >>> is_phone('(650) 952-6672')
    True
    >>> is_phone('(650) 952-66729')
    False
    >>> is_phone('650 815-5309')
    False
    >>> is_phone('650  815-5309')
    False

    '''
    pattern = re.compile(r'^\(\d{3}\)\s{1}\d{3}-\d{4}$')
    return pattern.search(phone) is not None

doctest.run_docstring_examples(is_phone, globals())
print(is_phone('(650) 815-5309')) # => True
print(is_phone('650.815.5309')) # => False

# quiz 8
s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1

print(list(d.items()))
