numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
           "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundred = "hundred"
thousand = "thousand"


def wordify(n, word=""):
    if n < 20:
        if len(word) > 0:
            return word + numbers[n] if n > 0 else word
        else:
            return numbers[n]
        return word + numbers[n]
    elif n < 100:
        tenwords = word + tens[n // 10]
        if n % 10 == 0:
            return tenwords
        else:
            return wordify(n % 10, tenwords + " ")
    elif n < 1000:
        hundredwords = word + numbers[n // 100] + " " + hundred
        if n % 100 == 0:
            return hundredwords
        else:
            return wordify(n % 100, hundredwords + " and ")
    elif n == 1000:
        return numbers[1] + " " + thousand


def totlen(n):
    sumlen = 0
    for i in range(1, n + 1):
        sumlen += len(wordify(i).replace(" ", ""))
        print(wordify(i))
        print(len(wordify(i)))
    return sumlen

print(totlen(1000))

