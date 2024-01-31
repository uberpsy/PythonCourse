student_scores = {
    'Ivan' : 5,
    'Alex' : 3.5,
    'Maria' : 5.5,
    'Georgy' : 5
}
 
for k,v in student_scores.items():
    if v >=4 :
        print(f'{k} - {v}')