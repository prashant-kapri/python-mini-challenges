# --------------
#Code starts here
def palindrome(num):
    n=[]
    for i in range(num+1,num*num):
        temp=i;
        rev=0
        while(i>0):
            rev=rev*10+i%10
            i=i//10
        if(rev==temp):
            n.append(rev)
        i+=1
    
    return(n[0])       

  





# --------------
def a_scramble(str_1,str_2):
    x= str_1
    y= str_2
    x=x.lower()
    y=y.lower()
    a=[i for i in x]
    b=[i for i in y]
    flag=1
    for i in b:
        if(i in a):
            a.remove(i)
        elif(i not in a):
            flag=0
    if(flag==1):
        return True
    else:
        return False


# --------------
def check_fib(num):
    a=0;
    b=1;
    sum=0;
    flag=0
    result=[0,1]
    for i in range(1,20):
        sum=a+b;
        a=b;
        b=sum;
        result.append(sum)
    for i in result:
        if(num==i):
            flag=1
    if(flag==1):
        return True 
    else:
        return False


# --------------
#Code starts here
def compress(word):
    word = word.lower()
    at = []
    st = [x for x in word]
    i=1
    while (i<=len(st)-1):
        count = 1
        while(st[i-1]==st[i]):
            count=count + 1
            i = i+1
            if(i==len(st)):
                break
        at.append(st[i-1])
        at.append(count)
        i= i+1
    ans = ""
    if(st[len(st)-1]!=st[len(st)-2]):
            at.append(st[len(st)-1])
            at.append(1)
    for i in at:
        ans+=str(i)
    return ans



# --------------
#Code starts here
def k_distinct(string,k):
    char=[]
    string=string.lower()
    res=[x for x in string]
    for i in range(0,len(res)):
        if(res[i] not in char):
            char.append(res[i])
    if(len(char)==k):
        return True
    else:
        return False


