total_seg_str = input ("Por favor, entre com o número de segundos que deseja converter:")
total_seg = int (total_seg_str)

days = (total_seg // (3600*24))
rdays = (total_seg % (3600*24))
hours = (rdays // 3600)
rhours = (rdays % 3600)
minutes = (rhours // 60)
seconds = (rhours % 60)

print (days,"dias,",hours,"horas,",minutes,"minutos e",seconds, "segundos." )
