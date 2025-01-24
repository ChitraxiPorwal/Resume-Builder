from fpdf import FPDF

lines = "=" * 150
print(lines)
print("Welcome to Resume Builder\n")
print("Enter all your details correctly and precisely\n")

# -------------------Personal Details -----------------------------------
print("\n*************************Enter your Personal Details*************************\n")
name = input("Please enter your full name: ")
email = input("Enter your emailId: ")
phone = int(input("Enter Phone no.: "))
linkedin = input("Enter your Linkedin Id: ")
github = input("Enter your GithubId: ")


def personalDetails():
    return f"\n Personal Details \n {name} \n {email} \n {phone} \n {linkedin} \n {github}\n"

# ----------Educational Details---------------------

print("\n*************************Enter your Educational Details*************************\n")

z = institution = education = marks = None
institution = []
educations = []
marks = []

eduans = 'y'
while (eduans == 'y'):
    eduans = input("Do you want to include your work experiences y or n:")
    z = eduans.strip().lower()
    if z == 'y':
        ins = input("\nEnter institution name:")
        institution.append(ins)
        edu = input("Enter education:")
        educations.append(edu)
        mar = input("Enter Marks:")
        marks.append(mar)

    elif eduans == 'n':
        break
    else:
        print("invalid input")


def education():
    if company and job:
        return "\n\n Educational Details\n" + "\n".join(f"- {ins}" for ins in institution) + "\n".join(f"- {ed}" for ed in educations) + "\n".join(f"- {m}" for m in marks)


# ----------------------------------------------------------Work Experiences--------------------------------------------------------------------------
print("\n*************************Enter your Work Experiences:*************************\n")
z = companyName = jobTitle = None
company = []
job = []
workans = 'y'
while (workans == 'y'):
    workans = input("Do you want to include your work experiences y or n:")
    z = workans.strip().lower()
    if z == 'y':
        companyName = input("\nEnter company name:")
        company.append(companyName)
        jobTitle = input("Enter job title:")
        job.append(jobTitle)
    elif workans == 'n':
        break
    else:
        print("invalid input")
def experience():
    if company and job:
        return "\n\n Work Experiences\n" + "\n".join(f"- {c}" for c in company)+"\n".join(f"- {j}" for j in job)

# ----------------------------------------------------------Academic Projects--------------------------------------------------------------------------
print("\n*************************Enter your projects:*************************\n")
project = tech = desc = w = None
proj = []
te = []
de = []
projans = 'y'
while (projans == 'y'):
    projans = input("Do you want to include your Projescts details enter y or n:")
    w = projans.strip().lower()
    if w == 'y':
        project = input("Enter the project name:")
        proj.append(project)
        tech = input("Enter the technology used:")
        te.append(tech)
        desc = input("Enter a short description of your project:")
        de.append(desc)
def projects():
    if proj and te and de:
        return "\n\n Projects\n" + "\n".join(f"- {p}" for p in proj) + "\n".join(f"- {e}" for e in te) + "\n".join(f"- {i}" for i in de)

# ------------Awards and Achievements------------------------------
print("\n*************************Enter description of your awards and achievments in short:*************************\n")
desc = p = None
ds = []
awardsans = 'y'
while (awardsans == 'y'):
    awardsans = input("Do you want to include your awards and achievements enter y or n:")
    p = awardsans.strip().lower()
    if p == 'y':
        desc = input("\nEnter a short description of your Awards and Achievements :")
        ds.append(desc)
def awardsAndAchievements():
    if ds:
        return "\n\n Awards and Achievements\n" + "\n".join(f"- {d}" for d in ds)

# ------------------Skills-----------------------------------------
print("\n*************************Enter your Technical and other Skills*************************\n")
skills = s = None
sk=[]
skillans = 'y'
while (skillans == 'y'):
    skillans = input("Do you want to include your educational details enter y or n:")
    s = skillans.strip().lower()
    if s == 'y':
        skills = input("\nEnter your skills:")
        sk.append(skills)

def skills():
    if sk:
        return "\n\n Skills\n" + "\n".join(f"- {s}" for s in sk)

# -----------------------------Interests and Hobbies---------------------
print("\n*************************Enter your interests and hobbies*************************\n")
in_ho = i = None
inh=[]
interestans = 'y'
while(interestans == 'y'):
    interestans = input("Do you want to include your interests and hobbies enter y or n:")
    i = interestans.strip().lower()
    if i == 'y':
        in_ho = input("\nEnter a short description about your interests and hobbies :")
        inh.append(in_ho)

def interestsAndHobbies():
    if inh:
        return "\n\nInterests and Hobbies\n" + "\n".join(f"- {hobby}" for hobby in inh)

# --------------------Display----------------------------------------------------
def display():
    print("*************************RESUME*************************")
    dis = (personalDetails())
    dis += (education())
    dis += (experience())
    dis += (projects())
    dis += (awardsAndAchievements())
    dis += (skills())
    dis += (interestsAndHobbies())
    return dis

print(display())

# -------------------------------pdf-------------------------------------------------------

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=13)
resume_text = display()
for line in resume_text.split("\n"):
    pdf.cell(200, 10, txt=line, ln=True)
pdf.output("Re.pdf")
print("Resume generated successfully as 'Resume.pdf'")
