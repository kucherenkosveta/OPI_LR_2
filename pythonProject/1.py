import csv

with open('UNdata.csv', 'r', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    women = []
    men = []
    for row in data:
        if row[1] == "Female":
            women.append(int(row[5]))
        elif row[1] == "Male":
            men.append(int(row[5]))
    print(women)
    print('dgsdkgkfkgkfkgkfk', men)
    #print(f"Среднее значение зачисления женщин в высшее образование из топ 10 стран: "f"{np.mean(w)}")
    #print(f"Среднее значение зачисления мужчин в высшее образование из топ 10 стран: "f"{np.mean(m)}")
