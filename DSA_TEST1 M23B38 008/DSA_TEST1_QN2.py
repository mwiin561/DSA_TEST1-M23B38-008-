##listing the catholic and anglican martyrs separately
catholic_martyrs = ["Achileo Kiwanuka", "Adolphus Ludigo Mukasa", "Ambrosius", "Kibuuka", "Anatoli", "Kiriggwajjo", "Andrew Kaggwa", "Antanansio", "Bazzekuketta", "Bruno", "Sserunkuuma", "Charles Lwanga", "Denis", "Ssebuggwawo", "Wasswa", "Gonzaga Gonza", "Gyavira Musoke", "James", "Buuzaabalyaawo", "John Maria", "Muzeeyi", "Joseph Mukasa", "Kizito", "Lukka", "Baanabakintu", "Matiya Mulumba", "Mbaga Tuzinde", "Mugagga Lubowa", "Mukasa", "Kiriwawanvu", "Nowa Mawaggali", "Ponsiano", "Ngondwe"]
anglican_martyrs = ["Aaron Lubega", "Apollo Kivebulaya", "Eria Sebukyala", "Fredrick Kizza", "George Kizza", "James Hannington", "Janani Luwum", "Joseph", "Balikuddembe", "Kizito", "Mark Kakumba", "Matia Mulumba", "Nuhu Mbegu", "Robert", "Munyagayirwa", "Samwiri Mukasa", "Yefusa Namayanja", "Yohana Mukasa", "Yosefu Lugalama", "Yowana Kitaka", "Yowana Maria", "Mukasa", "Yowana Mukiibi", "Yusufu Lugalama", "Zakayo Lubega"]

##identifying and removing any repeted names
catholic_martyrs = list(set(catholic_martyrs))
anglican_martyrs = list(set(anglican_martyrs))

##creating a function(martyr_count) to acquire a martyr name and make it an argument and returning the group to which the martyr belongs
def martyr_count(name):
    if name in catholic_martyrs:
        return "Catholic"
    elif name in anglican_martyrs:
        return "Anglican"
    else:
        return "Not a martyr"


##using (martyr_count) to determine the group to which kizito belongs
print(martyr_count("Kizito")) 

##functon that returns true if the input matches names of the ug martyrs in both lists
def is_martyr(name):
    return name in catholic_martyrs or name in anglican_martyrs

print(is_martyr("Kizito")) 
print(is_martyr("Achileo Kiwanuka")) 
print(is_martyr("Fredrick Kizza"))
print(is_martyr("Not a martyr")) 