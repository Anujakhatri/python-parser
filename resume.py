#python program to convert into resume from python forms, 
class Resume:
    def __init__(self):
        self.name = ""
        self.bio = ""
        self.contact = {}  #KEY:VALUE → {"email": "anuja@gmail.com"}
        self.address = ""
        self.headline = ""
        self.photo = None
        self.resume_url = None
        self.education = [] 
        self.skills = [] #list stores many values → ["Python", "Django"]
        self.experience = []
        
    def generate_resume(self):
        resume = f"""
        ===== MY RESUME =====
        Name: {self.name}
        Bio: {self.bio}
        Contact: {self.contact}
        Address: {self.address}
        Headline: {self.headline}
        Photo: {self.photo}
        Resume URL: {self.resume_url}
        Education: {self.education}
        Skills: {self.skills}
        Experience: {self.experience}
        =====================
        """
        return resume
    
def get_details():
    """
    Function to get details for a resume.
    It will prompt the user to enter their name, bio, address, headline, photo, resume url, education, skills and experience.
    It will store all the details in a Resume object and return it.
    """
    
    my_resume = Resume()
    
    #fill single values
    my_resume.name = input("Enter name: ")
    my_resume.bio = input("Enter bio: ")
    my_resume.address = input("Enter address: ")
    my_resume.headline = input("Enter headline: ")
    my_resume.photo = input("Enter photo: ")
    my_resume.resume_url = input("Enter resume url: ")
    
    #fill dictionary values
    my_resume.contact["contact"] = input("Enter email: ")
        
    #fill list values
    edu =input("Enter education: ")
    my_resume.education.append(edu)
    
    skills = input("Enter skills: ")
    my_resume.skills= [s.strip() for s in skills.split(",")]
    
    exp = input ("Enter experience: ")
    my_resume.experience.append(exp)
    
    return my_resume

def print_resume(my_resume):
    print(my_resume.generate_resume())
    
if __name__ == "__main__":
    my_resume = get_details()
    print_resume(my_resume)