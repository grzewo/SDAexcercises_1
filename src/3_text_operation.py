def task1():
    """
    Function which receives a sequence of comma-separated numbers and generate a list which contains
    every number

    Input: string with comma separated numbers
    Output: list with all the numbers
    """
    pass


def task2():
    """
    Function that can accept two strings as input and print the string with maximum length in console. If two strings
    have the same length, then the function should print all strings line by line.

    Input: two strings
    Output: one or two strings
    """
    pass


def task3():
    """
    Function that take an object as input and prints its docs (__doc__) every sentence in one line.

    Input: name of object (e.g. int)
    Output: string ready to write.
    """
    pass


def task4():
    """
    Function that can accept two strings as input and print all the letters that are in both strings.

    Input: two strings
    Output: None
    """
    pass


def task5():
    """
    Function that transform given string to a string where all occurrences of its first char have been
    changed to '$', except the first char itself (e.g. "asdfasdffdsa" -> "asdf$sdffds$")

    Input: string
    Output: string
    """
    pass


def task6():
    """
    Given an email adress: username@companyname.com" format, function returns the user name
    of a given email address. (e.g. "gregory@sda.pl" -> "gregory")
    You may do it with or without regular expressions.

    Input: string
    Output: string
    """
    pass


def task7():
    """
    Given many email adresses separated by comma, function returns the user names separated by comma
    of a given emails address (e.g. "gregory@sda.pl,jan@google.com -> "gregory,jan")

    Input: string
    Output: string
    """
    pass


def task8():
    """
    Given a sequence of words separated by whitespace as input, function prints the words composed of digits only.
    E.g. "I am not 4 years old. I was born in 1993" -> "4" "1993"

    Input: string
    Output: None
    """


def task9():
    """
    Given a single ASCII code, print and return character as string

    Input: number
    Output: string
    """


def task10():
    """
    Given a many ASCII codes as string separated by space (e.g. "76 78"), print and return characters as string ("LN")

    Input: string
    Output: string
    """


def task11():
    """
    Given an email adress: username@companyname.com" format, function returns the company name
    of a given email address. (e.g. "gregory@sda.pl -> "sda")
    You might want to use function match() from regex library, but it's doable without it.

    Input: string
    Output: string
    """
    pass


def task12():
    """
    Function that take 3 comma separated 4 digit binary numbers and then check whether they
    are divisible by 5 or not. The numbers that are divisible by 5 are to be printed as 1, if not 0 should be returned

    Input: string with three 3 digit binary numbers (e.g. "1111,1110,1100")
    Output: string with 1 and 0 (e.g. 1,0,0 - because 1111 if 15 and it is divided by 5)
    """


def task14():
    """
    Function that finds the string similarity between two given strings. Here string similarity is defined as follows:
    1. Find shorter string
    2. Iterating through shrorter string check if there is such a letter in longer string (ignore case with multiple
    same letter in one string)
    3. Ratio between number found duplicates and length of longer string is ration
    Print it as percent
    E.g. "mouse use" -> 60%, 3 letter ("use") / 5 (length of longer string)
    Later you might improve it to work with duplicates

    Input: two strings
    Ouput: string with percentage
    """
    pass


def task15():
    """
    Function that accepts simple equations such as: "12+4", "10-5" and print and return the result as float

    Input: one string
    Ouput: float number
    """
    pass


def task16():
    """
    Function that checks the validity of password input by users.
    Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    3. At least 1 letter between [A-Z]
    4. At least 1 character from [$#@]
    5. Minimum length of transaction password: 6
    6. Maximum length of transaction password: 12
    Input: string with password
    Output: boolean if it meets the requirements
    """
    pass


if __name__ == '__main__':
    pass
