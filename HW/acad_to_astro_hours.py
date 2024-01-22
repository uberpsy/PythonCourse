astro_hour = 60
acad_hour = 40
pause = 15

# academical hours needed for the course
acad_course_hours = 64

# calculate astronomical hours including breaks
x = round((acad_course_hours*acad_hour+acad_course_hours//3*pause)/astro_hour)
print( x )