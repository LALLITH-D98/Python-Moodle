                             Uncommon words
A sentence is a string of single-space separated words where each word consists only of
lowercase letters.A word is uncommon if it appears exactly once in one of the sentences,
and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return
the answer in any order.
Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
Constraints:
1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
Note:
Use dictionary to solve the problem
For example:
Input Result
this apple is sweet
this apple is sour
sweet sour
a=input().split()
b=input().split()
c1,c2,l={},{},[]
for i in a:
 c1[i]=c1.get(i,0)+1
for j in b:
 c2[j]=c2.get(j,0)+1
for w,c in c1.items():
 if(c==1 and w not in b):
 l.append(w)
for w,c in c2.items():
 if(c==1 and w not in a):
 l.append(w)
print(*l)
