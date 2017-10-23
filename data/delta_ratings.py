def rating_difference(data, data2):
	dict_delta = {}
	if len(data) != len(data2):
		print "Ratings list should be of equal size"
		return

	for i in range(len(data2)):

		if data[i].split(':')[0].strip() != data2[i].split(':')[0].strip():
			print "Values weren't the same"
			return

		score1 = data[i].split(':')[-1].strip()
		score2 =  data2[i].split(':')[-1].strip()


		delta  = int(score1) - int(score2)

		if delta in dict_delta:
			dict_delta[delta] = dict_delta[delta] + 1
		else:
			dict_delta[delta] = 1

	return dict_delta 






data = None
with open('virustotal_report.txt') as f:
    data = f.read().split('\n')

data2 = None
with open('2virustotal_report.txt') as f:
   data2 = f.read().split('\n')

print rating_difference(data,data2)