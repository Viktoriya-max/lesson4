grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]] #<class 'list'>
students={'Johnni','Bilbo','Steve','Khendrik','Aaron'}
students_=list(students)
print(students_)
students__=students_.sort() #sort alphabetically
print(students_)
aa=float(sum(grades[0])/len(grades[0]))#average_rating 'Johnny'
bil=float(sum(grades[1])/len(grades[1]))#average_rating 'Bilbo'
jh=float(sum(grades[2])/len(grades[2]))#average_rating 'Steve'
kh=float(sum(grades[3])/len(grades[3]))#averaga_rating 'Khendrik'
stev=float(sum(grades[4])/len(grades[4]))#averaga_rating 'Aaron'
average_rating={}#created a dictionary
average_rating.update({students_[0]:aa,students_[1]:bil,students_[2]:jh,students_[3]:kh,students_[4]:stev})
print(average_rating)

