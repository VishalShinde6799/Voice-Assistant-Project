import random
import david

jokes={
0:"Have you played the updated kids’ game? I Spy With My Little Eye . . . Phone.",    
1:'A perfectionist walked into a bar…apparently, the bar wasn’t set high enough.',
2:'You know it is going to be a bad day when the letters in your alphabet soup spell D-I-S-A-S-T-E-R.',
3:'Did you hear about the monkeys who shared an Amazon account? They were Prime mates.',
4:'Don\'t use \'beef stew\' as a computer password. It\'s not stroganoff.',
5:'I have read and agree to the Terms & Conditions, the biggest lie of the century!!!',
6:'Have you heard of that new band “1023 Megabytes”? They’re pretty good, but they don’t have a gig just yet.',
7:'I just got fired from my job at the keyboard factory. They told me I wasn’t putting in enough shifts.',
8:' Why did the computer show up at work late?  "It had a hard drive."',
9:'Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.',
10:"Autocorrect has become my worst enema.",
11:"The guy who invented predictive text died last night. His funfair is next monkey.",
12:"You know you’re texting too much when… You type ppl instead of people in a letter.",
13:"You know you’re texting too much when…… you try to text, but you’re on a landline.",
14:"You know you’re texting too much when…… you say LOL in real life, instead of just laughing.",
15:"Client to designer: “It doesn’t really look purple. It looks more like a mixture of red and blue.” Source: clientsfromhell.net",
16:"The cool part about naming your kid is, you don’t have to add six numbers to make sure the name is available.",
17:"where do birds go when they lose their tails????.......to the Retailer",
18:" What do you call a cat that gets anything it wants????......Purrrrrrrr-suasive.",
19:"What does the narcissistic cat say as she looks in the mirror????....I am pawsitively gorgeous.",
20:"What do you call a cat with eight legs that likes to swim???? ....An octo-puss.",
21:"There were 10 cats in a boat and one jumped out. How many were left???? ....None, because they were all a bunch of copycats.",
22:"What do you call it when a cat wins first place at a dog show???? ....A cat-has-trophy.",
23:"Never criticize someone until you’ve walked a mile in their shoes. That way, when you criticize them, they won’t be able to hear you from that far away. Plus, you’ll have their shoes.",
24:"A lot of people cry when they cut onions..... The trick is not to form an emotional bond."
}

def jokeswille():
    in1=random.randint(0, len(jokes)-1)
    print(jokes[in1])
    #jarvis.speak(jokes[in1])
    return(str(jokes[in1]))

#if __name__== '__main__':
    #jokeswille()