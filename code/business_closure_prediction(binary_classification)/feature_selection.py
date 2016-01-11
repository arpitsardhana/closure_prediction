import os
import sys
import time
import csv
import matplotlib.pyplot as plt
import re
import operator
input_file = str(sys.argv[1])

p_type = {'lot':0,'street':0,'garage':0,'valet':0,'validated':0,'no_parking':0}
p_num =  {0:0,1:0,2:0,3:0,4:0,5:0}

s_dict = {0:0,1:0,2:0,3:0,4:0,5:0}
r_dict = {}

g_type = {'brunch':0,'dinner':0,'breakfast':0,'dancing':0,'groups':0,'lunch':0,'kids':0,'desert':0,'latenight':0,'none':0}
g_num  = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

price_dict = {1:0,2:0,3:0,4:0} 

am_dict    = {'intimate':0,'hipster':0,'casual':0,'divey':0,'classy':0,'touristy':0,'trendy':0,'romantic':0,'upscale':0,'no_ambience':0}
am_num  = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

noise_dict = {}

music_dict = {'live':0,'background':0,'karaoke':0,'video':0,'playlist':0,'dj':0,'jukebox':0,'none':0}
music_num  = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0} 

facility_dict = {'wifi':0,'24h_open':0,'alcohol':0,'smoking':0,'none':0}
facility_num  = {0:0,1:0,2:0,3:0,4:0} 

modelfile = "final_proj.csv"
def write_csv_from_dict(p_dict,filename):
	row = ['0','0']
	for key in p_dict:

		row[0] = key
		row[1] = p_dict[key] 
        	with open(filename,"ab") as myfile:
                	write = csv.writer(myfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
                	write.writerow(row)

def get_value(row,index):

	cat_val1 = row[index]
        cat_val = cat_val1.strip().replace(" ","")
        cat_val = cat_val.replace("[","")
        cat_val = cat_val.replace("]","")
        cat_val = cat_val.replace("'","")
        cat_val = cat_val.replace("'","")
        cat_val = cat_val.lower()

	return cat_val


file_open = open(input_file,'r')
count = 0
cat_dict = dict()
filename = "openrestaurants.csv"
count = 0
count_f = 0
string = "restaurants"
with open(input_file, 'rb') as f:
     for row in csv.reader(f, delimiter=','):
             #print '|'.join(row)
	if count == 0:
		count += 1
		p_lot = row.index("attributes.Parking.lot")
		p_street = row.index("attributes.Parking.street")
		p_garage = row.index("attributes.Parking.garage")
		p_valet  = row.index("attributes.Parking.valet")
		p_validated = row.index("attributes.Parking.validated")

		g_brunch = row.index("attributes.Good For.brunch")
		g_dinner = row.index("attributes.Good For.dinner")
		g_breakfast = row.index("attributes.Good For.breakfast")
		g_dancing   = row.index("attributes.Good For Dancing")
		g_groups    = row.index("attributes.Good For Groups")		
		g_lunch = row.index("attributes.Good For.lunch")
		g_kids  = row.index("attributes.Good For Kids")
		g_desert = row.index("attributes.Good For.dessert")
		g_latenight = row.index("attributes.Good For.latenight")

		r_count = row.index("review_count")

		s_stars  = row.index("stars")

		asc_alcohol = row.index("attributes.Alcohol")
		asc_smoking = row.index("attributes.Smoking")

		price_range = row.index("attributes.Price Range")

		m_live      = row.index("attributes.Music.live")
		m_back      = row.index("attributes.Music.background_music")
		m_karaoke   = row.index("attributes.Music.karaoke")
		m_video     = row.index("attributes.Music.video")
		m_playlist  = row.index("attributes.Music.playlist")
		m_dj        = row.index("attributes.Music.dj")
		m_juke      = row.index("attributes.Music.jukebox")

		am_wifi     = row.index("attributes.Wi-Fi")
		am_int      = row.index("attributes.Ambience.intimate")		
		am_hip      = row.index("attributes.Ambience.hipster")
		am_cas      = row.index("attributes.Ambience.casual")
		am_noise    = row.index("attributes.Noise Level")
		am_dicey    = row.index("attributes.Ambience.divey")
		am_classy   = row.index("attributes.Ambience.classy")	
		am_tourity  = row.index("attributes.Ambience.touristy")
		am_trendy   = row.index("attributes.Ambience.trendy")
		am_romantic = row.index("attributes.Ambience.romantic")
		am_upscale  = row.index("attributes.Ambience.upscale")


		h_24h        = row.index("attributes.Open 24 Hours")


		category = row.index("categories")
		isopen = row.index("open")
	        with open(filename,"ab") as myfile:
       	        	write = csv.writer(myfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
       	        	write.writerow(row)

		continue

	
	#try:
	cat_val = get_value(row,isopen) 
	cat_val1 = get_value(row,category)
	p_lot_val = get_value(row,p_lot)
	p_street_val = get_value(row,p_street)
	p_garage_val = get_value(row,p_garage)
	p_valet_val = get_value(row,p_valet)
	p_validated_val = get_value(row,p_validated)
	s_stars_val = get_value(row,s_stars)
	r_count_val = get_value(row,r_count)
	g_brunch_val = get_value(row,g_brunch)
	g_dinner_val = get_value(row,g_dinner)
	g_breakfast_val = get_value(row,g_breakfast)
	g_dancing_val   = get_value(row,g_dancing)
	g_groups_val    = get_value(row,g_groups)
	g_lunch_val     = get_value(row,g_lunch)
	g_kids_val      = get_value(row,g_kids)
	g_desert_val    = get_value(row,g_desert)
	g_latenight_val     = get_value(row,g_latenight)

	am_int_val = get_value(row,am_int)
	am_hip_val = get_value(row,am_hip)
	am_cas_val = get_value(row,am_cas)
	am_dicey_val = get_value(row,am_dicey)
	am_classy_val = get_value(row,am_classy)
	am_tourity_val = get_value(row,am_tourity)
	am_trendy_val = get_value(row,am_trendy)
	am_romantic_val = get_value(row,am_romantic)
	am_upscale_val = get_value(row,am_upscale)

	noise_level_val = get_value(row,am_noise)
	price = get_value(row,price_range)


	m_live_val = get_value(row,m_live)
	m_back_val = get_value(row,m_back)
	m_karaoke_val = get_value(row,m_karaoke)
	m_video_val = get_value(row,m_video)
	m_playlist_val = get_value(row,m_playlist)
	m_dj_val = get_value(row,m_dj)
	m_juke_val = get_value(row,m_juke)

	fac_val_alcohol = get_value(row,asc_alcohol)
	fac_val_smoking = get_value(row,asc_smoking) 
	fac_val_24h     = get_value(row,h_24h)
	fac_val_wifi    = get_value(row,am_wifi)
 
	#except:
	count_f += 1
	#continue

        #col =[0,0,0,0,0]	
	cat_list_temp = cat_val1.split(",")

	if cat_val == "false":
		closed = 1
	else:
		closed = 0
	if  string in cat_list_temp:
		count += 1
#evaluate parking
		p_count = 0
		p_flag = 0

		if p_lot_val == "true":
			p_count += 1
			p_type['lot'] += 1
		
                if p_street_val == "true":
                        p_count += 1
                        p_type['street'] += 1

                if p_garage_val == "true":
                        p_count += 1
                        p_type['garage'] += 1

                if p_valet_val == "true":
                        p_count += 1
                        p_type['valet'] += 1

                if p_validated_val == "true":
                        p_count += 1
                        p_type['validated'] += 1

		if p_count == 0:
			p_type['no_parking'] += 1
		else:
			p_flag = 1

		
		p_num[p_count] += 1

		#col[5] = p_count
#evaluate stars and review
                s_value = int(round(float(s_stars_val)))
		s_dict[s_value] += 1

		r_value = int(round(float(r_count_val),-1))
	

		if r_value > 100 :
			r_value = 110

		if r_dict.has_key(r_value):
			r_dict[r_value] += 1
		else:
			r_dict[r_value] = 1 

		#col[1] = r_value	
		#col[2] = s_value	
#evaluate good for
		g_count = 0
		lunch_flag = 0
		group_flag = 0
		dinner_flag =0
		
		if g_brunch_val == "true":
			g_count += 1
			g_type['brunch'] += 1

                if g_dinner_val == "true":
                        g_count += 1
                        g_type['dinner'] += 1
			dinner_flag = 1

                if g_breakfast_val == "true":
                        g_count += 1
                        g_type['breakfast'] += 1

                if g_dancing_val == "true":
                        g_count += 1
                        g_type['dancing'] += 1

                if g_groups_val == "true":
                        g_count += 1
                        g_type['groups'] += 1
			group_flag = 1

                if g_lunch_val == "true":
                        g_count += 1
                        g_type['lunch'] += 1
			lunch_flag = 1

                if g_kids_val == "true":
                        g_count += 1
                        g_type['kids'] += 1

                if g_desert_val == "true":
                        g_count += 1
                        g_type['desert'] += 1

                if g_latenight_val == "true":
                        g_count += 1
                        g_type['latenight'] += 1

		if g_count == 0:
			g_type['none'] += 1

		g_num[g_count] += 1
		#col[6] = g_count


		

#evaluate price range
		#print price
		if len(price) != 0:
			p_value = int(price)
			price_dict[p_value] += 1
		else:
			p_value = 0
		
		#col[3]=p_value
#evalute ambience
		am_count = 0
		am_flag = 0
		if am_int_val == "true":
			am_count += 1
			am_dict['intimate'] += 1

                if am_hip_val == "true":
                        am_count += 1
                        am_dict['hipster'] += 1

                if am_cas_val == "true":
                        am_count += 1
                        am_dict['casual'] += 1

                if am_dicey_val == "true":
                        am_count += 1
                        am_dict['divey'] += 1

                if am_classy_val == "true":
                        am_count += 1
                        am_dict['classy'] += 1

                if am_tourity_val == "true":
                        am_count += 1
                        am_dict['touristy'] += 1

                if am_trendy_val == "true":
                        am_count += 1
                        am_dict['trendy'] += 1

                if am_romantic_val == "true":
                        am_count += 1
                        am_dict['romantic'] += 1

                if am_upscale_val == "true":
                        am_count += 1
                        am_dict['upscale'] += 1

                if am_count == 0:
                        am_count += 1
                        am_dict['no_ambience'] += 1
		else:
			am_flag = 1

		am_num[am_count] += 1
		#col[7] = am_count
 

#evalute noise level
		if noise_dict.has_key(noise_level_val):
			noise_dict[noise_level_val] += 1
		else:
			noise_dict[noise_level_val] = 1

		if noise_level_val == "not_available":
			x = 0
		elif noise_level_val == "very_loud":
			x = 1
		elif noise_level_val == "loud":
			x = 2
		elif noise_level_val == "average":
			x = 3
		elif noise_level_val == "quiet":
			x = 4

		#col[4] = x

	

#evaluate music taste
		m_count = 0
		if m_live_val == "true":
			m_count += 1
			music_dict['live'] += 1

                if m_back_val == "true":
                        m_count += 1
                        music_dict['background'] += 1

                if m_karaoke_val == "true":
                        m_count += 1
                        music_dict['karaoke'] += 1

                if m_video_val == "true":
                        m_count += 1
                        music_dict['video'] += 1

                if m_playlist_val == "true":
                        m_count += 1
                        music_dict['playlist'] += 1

                if m_dj_val == "true":
                        m_count += 1
                        music_dict['dj'] += 1

                if m_juke_val == "true":
                        m_count += 1
                        music_dict['jukebox'] += 1

                if m_count == 0:
                        music_dict['none'] += 1

		music_num[m_count] += 1

		#col[8] = m_count

		

#evaluate other facilities
		fac_count = 0

		if fac_val_alcohol == "true":
			fac_count += 1
			facility_dict['alcohol'] += 1

                if fac_val_smoking == "true":
                        fac_count += 1
                        facility_dict['smoking'] += 1

                if fac_val_24h == "true":
                        fac_count += 1
                        facility_dict['24h_open'] += 1

                if fac_val_wifi == "true":
                        fac_count += 1
                        facility_dict['wifi'] += 1

                if fac_count == 0: 
                        facility_dict['none'] += 1

		facility_num[fac_count] += 1

		col =[0,0,0,0,0,0,0,0,0,0,0]	
		col[0] = closed	
		col[1] = r_value
		col[2] = s_value
		col[3] = p_value
		col[4] = x
		col[5] = am_flag
		col[6] = lunch_flag
		col[7] = group_flag
		col[8] = dinner_flag
		col[9]  = p_flag
		#col[4] = p_count
		col[10] = g_count
		#col[6] = am_count
		#col[7] = m_count

                with open(modelfile,"ab") as myfile:
                        write = csv.writer(myfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
                        write.writerow(col)





file_open.close()
#print p_type
#print p_num
print count
print count_f
#print s_dict
#print r_dict
#print price_dict
#print noise_dict
#print g_type
#print g_num
#print am_dict
#print am_num
#print music_dict
#print music_num
#print facility_dict
#print facility_num

#write_csv_from_dict(p_type,"p_type.csv")
#write_csv_from_dict(p_num,"p_num.csv")
#write_csv_from_dict(s_dict,"stars.csv")
#write_csv_from_dict(r_dict,"review_count.csv")
#write_csv_from_dict(price_dict,"price_range.csv")
#write_csv_from_dict(noise_dict,"noise_range.csv")
#write_csv_from_dict(g_type,"g_type.csv")
#write_csv_from_dict(g_num,"g_num.csv")
#write_csv_from_dict(am_dict,"am_dict.csv")
#write_csv_from_dict(am_num,"am_num.csv")
#write_csv_from_dict(music_dict,"music_dict.csv")
#write_csv_from_dict(music_num,"music_num.csv")
#write_csv_from_dict(facility_dict,"facility_dict.csv")
#write_csv_from_dict(facility_num,"facility_num.csv")




