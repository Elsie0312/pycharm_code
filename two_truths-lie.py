print('Welcome to Two Truths and a Lie! /n One of the following statements is a lie...you need to identify which one!')
print('1. I have a donkey living in my backyard.')
print('2. I have three fur babies')
print('3. I speak 4 languages')

truth_or_lie = input('Now put in the number of the statement you think is the lie!')

conv_truth_or_lie = int(truth_or_lie)

if conv_truth_or_lie == 1:
    print('Congrats, you have identified the lie correctly!')

elif conv_truth_or_lie == 2:
	print('That is not the one!')

elif conv_truth_or_lie == 3:
	print('Sorry, you have to try again')
