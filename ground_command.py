import csv
from datetime import datetime
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.ttk
########################################################################################################################
temp = 0.00
altitude = 0.00
pressure = 0.00
habitat_alt = 0.00
water_alt = 0.00
glider_alt = 0.00
coords = [0.00, 0.00]     # GPS [latitude, longitude]
acc_x = 0.00
acc_y = 0.00
acc_z = 0.00
mag_x = 0.00
mag_y = 0.00
mag_z = 0.00
gyro_x = 0.00
gyro_y = 0.00
gyro_z = 0.00
gps_lat = 0.00
gps_lon = 0.00
gps_spd = 0.00
send_data = "00"
pay_drop = False
glide_drop = False

file_in = "from_the_air.txt"
file_out = "from_ground_command.txt"

data_out_file = open(file_out, 'w')
data_out_file.write("00")
data_out_file.close()

dt = str(datetime.now().strftime("test_data/%d_%m_%Y_%H_%M.csv"))
data_save = open(dt, "w+")
data_save.close()

########################################################################################################################
#   base_width = 680
#   gps_map = tk.PhotoImage(file="airfield_test.jpg")            # GPS map file
#   gps_map = gps_map.resize((680, 410), Image.ANTIALIAS)
#   gps_map = ImageTk.PhotoImage(gps_map)
########################################################################################################################


def drop_payload():
    global pay_drop
    if pay_drop is False:
        pay_drop = True
        global habitat_alt
        global water_alt
        habitat_alt = altitude
        water_alt = altitude
        print("Payloads Dropped")
    else:
        print("Payloads Already Dropped")


def drop_glider():
    global glide_drop
    if glide_drop is False:
        glide_drop = True
        global glider_alt
        glider_alt = altitude
        print("Glider Dropped")
    else:
        print("Glider Already Dropped")


def parse_data(formatted_data):
    global altitude
    global temp
    global pressure
    global acc_x
    global acc_y
    global acc_z
    global mag_x
    global mag_y
    global mag_z
    global gyro_x
    global gyro_y
    global gyro_z
    global gps_lat
    global gps_lon
    global gps_spd

    str_temp = formatted_data[0:4].replace("n", "")
    str_pressure = formatted_data[5:11].replace("n", "")
    str_altitude = formatted_data[12:16].replace("n", "")
    str_acc_x = formatted_data[17:22].replace("n", "")
    str_acc_y = formatted_data[23:28].replace("n", "")
    str_acc_z = formatted_data[29:34].replace("n", "")
    str_mag_x = formatted_data[35:40].replace("n", "")
    str_mag_y = formatted_data[41:46].replace("n", "")
    str_mag_z = formatted_data[47:52].replace("n", "")
    str_gyro_xf = formatted_data[53:58].replace("n", "")
    str_gyro_yf = formatted_data[59:64].replace("n", "")
    str_gyro_zf = formatted_data[65:70].replace("n", "")
    str_gps_lat = formatted_data[71:78].replace("n","")
    str_gps_lon = formatted_data[79:86].replace("n", "")
    str_gps_spd = formatted_data[87:90].replace("n", "")
    try:
        temp = float(str_temp) / 100
        pressure = float(str_pressure)
        altitude = round((float(str_altitude) / 100) * 3.28, 2)
        acc_x = float(str_acc_x) / 100
        acc_y = float(str_acc_y) / 100
        acc_z = float(str_acc_z) / 100
        mag_x = float(str_mag_x) / 100
        mag_y = float(str_mag_y) / 100
        mag_z = float(str_mag_z) / 100
        gyro_x = float(str_gyro_xf) / 100
        gyro_y = float(str_gyro_yf) / 100
        gyro_z = float(str_gyro_zf) / 100
        gps_lat = float(str_gps_lat) / 1000000
        gps_lat = float(str_gps_lon) / 1000000
        gps_spd = float(str_gps_spd) / 1000000
    except:
        print("str to float error")

    #   print(str_temp, str_pressure, str_altitude, str_acc_x, str_acc_y, str_acc_z,
    #      str_mag_x, str_mag_y, str_mag_z, str_gyro_x, str_gyro_y, str_gyro_z)

    #   print(temp, pressure, altitude, acc_x, acc_y, acc_z, mag_x, mag_y, mag_z, gyro_x, gyro_y, gyro_z)

    return (str(temp)+","+str(pressure)+","+str(altitude)+","+str(acc_x)+","+str(acc_y)+","+str(acc_z)+","+str(mag_x)+
            ","+str(mag_y)+","+str(mag_z)+","+str(gyro_x)+","+str(gyro_y)+","+str(gyro_z)+",")


root = tk.Tk()
root.title("Data Acquisition System")
root.geometry("1440x900")
root.configure(background='black')             # GUI Setup
frame1_bg = "grey"
frame2_bg = "grey"
frame3_bg = "grey"
frame4_bg = "grey"

#   Dynamic variables
str_alt = tk.StringVar()
str_alt.set(altitude)
str_glider_alt = tk.StringVar()
str_glider_alt.set(glider_alt)
str_habitat_alt = tk.StringVar()
str_habitat_alt.set(habitat_alt)
str_water_alt = tk.StringVar()
str_water_alt.set(water_alt)
str_gyro_x = tk.StringVar()
str_gyro_x.set(gyro_x)
str_gyro_y = tk.StringVar()
str_gyro_y.set(gyro_y)
str_gyro_z = tk.StringVar()
str_gyro_z.set(gyro_z)
str_lat = tk.StringVar()
str_lat.set(gps_lat)
str_lon = tk.StringVar()
str_lon.set(gps_lon)
str_spd = tk.StringVar()
str_spd.set(gps_spd)

tl_frame = tk.Frame(root, background=frame1_bg, width=720, height=450, highlightbackground="black",
                    highlightcolor="black", highlightthickness=1)
tr_frame = tk.Frame(root, background=frame2_bg, width=720, height=450, highlightbackground="black",
                    highlightcolor="black", highlightthickness=1)
bl_frame = tk.Frame(root, background=frame3_bg, width=720, height=450, highlightbackground="black",
                    highlightcolor="black", highlightthickness=1)
br_frame = tk.Frame(root, background=frame4_bg, width=720, height=450, highlightbackground="black",
                    highlightcolor="black", highlightthickness=1)

tl_frame.grid_propagate(0)
tr_frame.grid_propagate(0)
bl_frame.grid_propagate(0)
br_frame.grid_propagate(0)

tl_frame.grid(row=1)
bl_frame.grid(row=2)
tr_frame.grid(row=1, column=2)
br_frame.grid(row=2, column=2)

#   Frame 1: Altitude and Speed
alt_label = tk.Label(tl_frame, text="Altitude:", font=("Helvetica", 48), bg=frame1_bg)
alt_unit = tk.Label(tl_frame, text="ft", font=("Helvetica", 48), bg=frame1_bg)
alt_num = tk.Label(tl_frame, textvariable=str_alt, font=("Helvetica", 48), bd=5, relief="sunken")
speed_label = tk.Label(tl_frame, text="Speed:", font=("Helvetica", 48), bg=frame1_bg)
speed_unit = tk.Label(tl_frame, text="mph", font=("Helvetica", 48), bg=frame1_bg)
speed_num = tk.Label(tl_frame, textvariable=str_spd, font=("Helvetica", 48), bd=5, relief="sunken")
alt_label.grid(row=1, sticky="nesw")
alt_num.grid(row=1, column=2, sticky="nesw")
alt_unit.grid(row=1, column=3, sticky="nsw")
speed_label.grid(row=2, sticky="nesw")
speed_num.grid(row=2, column=2, sticky="nesw")
speed_unit.grid(row=2, column=3, sticky="nsw")

#   Frame 2: Habitat, Water, and Glider
h_alt_label = tk.Label(tr_frame, text="Habitat Altitude:", font=("Helvetica", 36), bg=frame2_bg)
w_alt_label = tk.Label(tr_frame, text="Water Altitude:", font=("Helvetica", 36), bg=frame2_bg)
g_alt_label = tk.Label(tr_frame, text="Glider Altitude:", font=("Helvetica", 36), bg=frame2_bg)
h_alt_num = tk.Label(tr_frame, textvariable=str_habitat_alt, font=("Helvetica", 48), bd=5, relief="sunken")
w_alt_num = tk.Label(tr_frame, textvariable=str_water_alt, font=("Helvetica", 48), bd=5, relief="sunken")
g_alt_num = tk.Label(tr_frame, textvariable=str_glider_alt, font=("Helvetica", 48), bd=5, relief="sunken")
h_alt_unit = tk.Label(tr_frame, text="ft", font=("Helvetica", 36), bg=frame2_bg)
w_alt_unit = tk.Label(tr_frame, text="ft", font=("Helvetica", 36), bg=frame2_bg)
g_alt_unit = tk.Label(tr_frame, text="ft", font=("Helvetica", 36), bg=frame2_bg)
drop_label = tk.Label(tr_frame, text="Drop", font=("Helvetica", 32), bg=frame2_bg)
space_label = tk.Label(tr_frame, text="   ", font=("Helvetica", 32), bg=frame2_bg)
payload_drop_button = tk.Button(tr_frame, text="  ", font=("Helvetica", 36), borderwidth=4, command=drop_payload)
glider_drop_button = tk.Button(tr_frame, text="  ", font=("Helvetica", 36), borderwidth=4, command=drop_glider)

drop_label.grid(row=1, column=4)
space_label.grid(row=1, column=3)
h_alt_label.grid(row=3, sticky="nesw")
w_alt_label.grid(row=2, sticky="nesw")
g_alt_label.grid(row=4, sticky="nesw")
h_alt_num.grid(row=2, column=2, sticky="nesw")
w_alt_num.grid(row=3, column=2, sticky="nesw")
g_alt_num.grid(row=4, column=2, sticky="nesw")
h_alt_unit.grid(row=2, column=3, sticky="nsw")
w_alt_unit.grid(row=3, column=3, sticky="nsw")
g_alt_unit.grid(row=4, column=3, sticky="nsw")
payload_drop_button.grid(row=2, rowspan=2, column=4, pady=10, sticky="nesw")
glider_drop_button.grid(row=4, column=4, pady=10, sticky="nesw")

#   Frame 3: GPS
gps_display = tk.Canvas(bl_frame, width=690, height=420, background="white")
gps_display.place(x=12, y=12)
gps_map = ImageTk.PhotoImage(Image.open("formatted_airfield_test.JPG"))
gps_display.create_image(10, 10, image=gps_map, anchor="nw")

#   Frame 4: Gyro
gyro_display = tk.Canvas(br_frame, width=400, height=420, background="white")
roll_label = tk.Label(br_frame, font=("Helvetica", 24), text="Roll:", bg=frame4_bg)
pitch_label = tk.Label(br_frame, font=("Helvetica", 24), text="Pitch:", bg=frame4_bg)
yaw_label = tk.Label(br_frame, font=("Helvetica", 24), text="Yaw:", bg=frame4_bg)
roll_num = tk.Label(br_frame, font=("Helvetica", 24), textvariable=str_gyro_x, bd=5, relief="sunken")
pitch_num = tk.Label(br_frame, font=("Helvetica", 24), textvariable=str_gyro_y, bd=5, relief="sunken")
yaw_num = tk.Label(br_frame, font=("Helvetica", 24), textvariable=str_gyro_z, bd=5, relief="sunken")
roll_unit = tk.Label(br_frame, text="degrees ("+u'\u00b0'+")", font=("Helvetica", 16), bg=frame4_bg)
pitch_unit = tk.Label(br_frame, text="degrees ("+u'\u00b0'+")", font=("Helvetica", 16), bg=frame4_bg)
yaw_unit = tk.Label(br_frame, text="degrees ("+u'\u00b0'+")", font=("Helvetica", 16), bg=frame4_bg)

roll_label.grid(row=1)
pitch_label.grid(row=2)
yaw_label.grid(row=3)
roll_num.grid(row=1, column=2)
pitch_num.grid(row=2, column=2)
yaw_num.grid(row=3, column=2)
roll_unit.grid(row=1, column=3, sticky="nsw")
pitch_unit.grid(row=2, column=3, sticky="nsw")
yaw_unit.grid(row=3, column=3, sticky="nsw")
gyro_display.place(x=300, y=12)

while True:
    #############################################################
    #   Updates
    data_in_file = open(file_in)
    data_in = data_in_file.read()
    data_in_file.close()
    data_save = open(dt, "a+")

    if pay_drop and glide_drop is True:
        send_data = "11"
    elif pay_drop is True:
        send_data = "10"
    elif glide_drop is True:
        send_data = "01"

    data_out_file = open(file_out, 'w')
    data_out_file.write(send_data)
    data_out_file.close()

    formatted_data_in = parse_data(data_in)

    data_save.write(formatted_data_in+'\n')

    str_alt.set(altitude)
    str_spd.set(gps_spd)
    str_glider_alt.set(glider_alt)
    str_habitat_alt.set(habitat_alt)
    str_water_alt.set(water_alt)
    str_gyro_x.set(gyro_x)
    str_gyro_y.set(gyro_y)
    str_gyro_z.set(gyro_z)
    str_lat.set(gps_lat)
    str_lon.set(gps_lon)

    #############################################################
    root.update_idletasks()
    root.update()
