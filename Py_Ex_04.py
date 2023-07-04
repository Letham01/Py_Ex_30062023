settings = {'title': 'My original title'}

def change_site_title(new_title):
    """Changes the title in the global settings dictionary"""
    global settings
    settings['title'] = new_title

# Test case
print(settings)
change_site_title("A new fancy title")
print(settings)

#----------------------------

settings = {'title': 'My original title'}
default_settings = {'title': 'My original title'}

def change_site_title(new_title):
    """Changes the title in the global settings dictionary"""
    global settings
    settings['title'] = new_title

def get_title(dictionary=default_settings):
    """Returns the value of the 'title' key in the given dictionary"""
    return dictionary['title']

# Test 
print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())

#----------------------------

settings = {'title': 'My original title', 'pages': []}
default_settings = {'title': 'My original title', 'pages': []}

def change_site_title(new_title):
    """Changes the title in the global settings dictionary"""
    global settings
    settings['title'] = new_title

def get_title(dictionary=default_settings):
    """Returns the value of the 'title' key in the given dictionary"""
    return dictionary['title']

def get_pages(settings=default_settings):
    """Returns the list stored in the 'pages' key of the given settings dictionary"""
    return settings['pages']

def add_page(page, settings=default_settings):
    """Appends the given page dictionary to the 'pages' key of the given settings dictionary"""
    settings['pages'].append(page)

# Test 
home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))

#-------------------------

def print_user_profile(gender='female', first=None, last='Doe', pictures=[]):
    """Prints the user profile including the name and list of pictures"""
    header_picture = 'common_header.png'
    print(f"The user {first or ('John' if gender == 'male' else 'Jane')} {last} has the following pictures:")
    print(header_picture)
    for picture in pictures:
        print(picture)

# Test cases
test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)
