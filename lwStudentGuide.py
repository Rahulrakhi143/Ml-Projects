def guide_student_by_subject(subject):
    subject = subject.lower()

    guidance = {
        "math": [
            "Engineer",
            "Data Scientist",
            "Mathematician",
            "Actuary",
            "Economist"
        ],
        "science": [
            "Doctor",
            "Pharmacist",
            "Research Scientist",
            "Biotechnologist",
            "Environmentalist"
        ],
        "physics": [
            "Mechanical Engineer",
            "Physicist",
            "Astronomer",
            "Robotics Engineer"
        ],
        "chemistry": [
            "Chemical Engineer",
            "Pharmacologist",
            "Forensic Scientist",
            "Material Scientist"
        ],
        "biology": [
            "Doctor",
            "Geneticist",
            "Zoologist",
            "Microbiologist"
        ],
        "computer": [
            "Software Engineer",
            "Web Developer",
            "AI/ML Engineer",
            "Cybersecurity Expert"
        ],
        "english": [
            "Journalist",
            "Content Writer",
            "Teacher",
            "Editor"
        ],
        "history": [
            "Historian",
            "Archaeologist",
            "Civil Services",
            "Museum Curator"
        ],
        "geography": [
            "Geologist",
            "Urban Planner",
            "Cartographer",
            "Environmental Consultant"
        ],
        "commerce": [
            "CA (Chartered Accountant)",
            "Banker",
            "Business Analyst",
            "Financial Advisor"
        ],
        "arts": [
            "Designer",
            "Animator",
            "Musician",
            "Fine Artist"
        ]
    }

    if subject in guidance:
        print(f"\n📘 Based on your interest in {subject.capitalize()}, you can explore:")
        for career in guidance[subject]:
            print(f" - {career}")
    else:
        print("\n⚠️ Sorry, guidance for this subject is not available.")
        print("Try subjects like: Math, Science, Physics, Computer, etc.")

# Main Program
subject = input("Enter your favorite subject: ")
guide_student_by_subject(subject)
