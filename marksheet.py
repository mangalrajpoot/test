#manage marksheet program with all possible exception

class MarksException(Exception):
    pass

class SubjectException(Exception):
    pass

try:
    m1=int(input('Enter Marks'))
    m2=int(input('Enter Marks'))
    m3=int(input('Enter Marks'))
    m4=int(input('Enter Marks'))
    m5=int(input('Enter Marks'))
    if m1<=0 and m1>100 or m2<=0 and m2>100 or m3<=0 and m3>100 or m4<=0 and m4>100 or m5<=0 and m5>100:
        raise MarksException
    else:
        total=m1+m2+m3+m4+m5
        print('Total Marks',total)
except MarksException:
    print('Marks must be between 0 to 100')
except ValueError:
    print('Please Enter Numeric Value')

try:
    s1=input('Enter Subject Name')
    s2=input('Enter Subject Name')
    s3=input('Enter Subject Name')
    s4=input('Enter Subject Name')
    s5=input('Enter Subject Name')
    if s1>='A' and s1<='Z' and s2>='A' and s2<='Z' and s3>='A' and s3<='Z' and s4>='A' and s4<='Z' and s5>='A' and s5<='Z':
        pass
    else:
        raise SubjectException
except SubjectException:
    print('Subject Name must start with capital letter')

    
        