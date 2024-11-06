#Problem 0: Building Management System
#Design and implement a simplified building management system using object-oriented programming principles.
# Create classes to represent tenants, rent, payment history, apartments, tenant information,
#policies, and reported maintenance requests.
#1. **Tenant Class:**
#- Create a `Tenant` class with attributes for tenant name, contact information, and lease start date.
#- Implement methods to display tenant information and update contact details.
#2. **Rent Class:**
#- Create a `Rent` class to track rent payments. Include attributes for payment amount, due date, and payment status (paid or overdue).
#- Implement methods to record rent payments and check payment status.
#3. **Apartment Class:**
#- Design an `Apartment` class to represent individual apartment units. Include attributes for apartment number, square footage, and rent amount.
#- Implement methods to display apartment details.
#4. **Tenant Information Class:**
#- Create a `TenantInformation` class to manage tenant profiles. Include attributes for tenant ID, lease history, and current apartment.
#- Implement methods to add tenants to the system, update lease history, and find tenant information.
#5. **Policy Class:**
#- Develop a `Policy` class to define building policies and rules. Include attributes for policy ID, description, and effective date.
#- Implement methods to list policies and check compliance.
#6. **Maintenance Request Class:**
#- Design a `MaintenanceRequest` class to track tenant-reported maintenance requests. Include attributes for request ID, description, status, and date reported.
#- Implement methods to record maintenance requests, update their status, and list open requests.
#**Tasks:**
#. Create the classes mentioned above, ensuring appropriate encapsulation and data validation where necessary.
#2. Implement functionality to list all tenants with overdue rent payments.
#3. Demonstrate the system's functionality by simulating interactions such as adding tenants, making rent payments,
# reporting maintenance requests, and checking compliance with policies.
#4. Implement tests cases accordingly

class Tenant:
    def __init__(self, name, contact_info, lease_start_date):
        self.name = name
        self.contact_info = contact_info
        self.lease_start_date = lease_start_date

    def display_info(self):
        return f"Tenant: {self.name}, Contact: {self.contact_info}, Lease Start: {self.lease_start_date}"

    def update_contact(self, new_contact_info):
        self.contact_info = new_contact_info


class Rent:
    def __init__(self, amount, due_date):
        self.amount = amount
        self.due_date = due_date
        self.payment_status = "unpaid"

    def record_payment(self, payment_date):
        # Simple lexicographical comparison for dates
        if payment_date <= self.due_date:
            self.payment_status = "paid"
        else:
            self.payment_status = "overdue"

    def check_payment_status(self):
        return self.payment_status


class Apartment:
    def __init__(self, apartment_number, square_meters, rent_amount):
        self.apartment_number = apartment_number
        self.square_meters = square_meters
        self.rent_amount = rent_amount

    def display_details(self):
        return f"Apartment {self.apartment_number}: {self.square_meters} square meters, Rent: EUR{self.rent_amount}"


class TenantInformation:
    def __init__(self):
        self.tenants = {}

    def add_tenant(self, tenant_id, tenant, apartment):
        self.tenants[tenant_id] = {
            "tenant": tenant,
            "apartment": apartment,
            "lease_history": []
        }

    def update_lease_history(self, tenant_id, lease_info):
        if tenant_id in self.tenants:
            self.tenants[tenant_id]["lease_history"].append(lease_info)

    def get_tenant_info(self, tenant_id):
        if tenant_id in self.tenants:
            tenant = self.tenants[tenant_id]["tenant"]
            apartment = self.tenants[tenant_id]["apartment"]
            lease_history = self.tenants[tenant_id]["lease_history"]
            return tenant.display_info() + f"\nApartment: {apartment.display_details()}\nLease History: {lease_history}"
        return "Tenant not found."


class Policy:
    def __init__(self, policy_id, description, effective_date):
        self.policy_id = policy_id
        self.description = description
        self.effective_date = effective_date

    def display_policy(self):
        return f"Policy {self.policy_id}: {self.description}, Effective from: {self.effective_date}"

    def check_compliance(self, tenant_lease_start_date):
        return tenant_lease_start_date >= self.effective_date


class MaintenanceRequest:
    def __init__(self, request_id, description, date_reported):
        self.request_id = request_id
        self.description = description
        self.status = "open"
        self.date_reported = date_reported

    def update_status(self, new_status):
        if new_status in ["open", "closed", "in-progress"]:
            self.status = new_status

    def display_request(self):
        return f"Request {self.request_id}: {self.description}, Status: {self.status}, Reported on: {self.date_reported}"


tenant1 = Tenant("Toshko Goshkov", "tosho@mail.com", "2024-11-03")
tenant2 = Tenant("Sasho Pehsov", "sasho@mail.com", "2024-11-05")

apartment1 = Apartment(43, 35, 500)
apartment2 = Apartment(59, 55, 800)

tenant_info = TenantInformation()
tenant_info.add_tenant(1, tenant1, apartment1)
tenant_info.add_tenant(2, tenant2, apartment2)

rent1 = Rent(500, "2025-11-01")
rent2 = Rent(800, "2025-11-02")

rent_records = {1: rent1, 2: rent2}

rent1.record_payment("2024-11-03")  # Paid
rent2.record_payment("2024-11-07")  # Overdue

maintenance_request1 = MaintenanceRequest(1, "Washing machine broken", "2024-11-04")
maintenance_request1.update_status("in-progress")  # Correct status

def list_overdue_rent(tenant_info, rent_records):
    overdue_tenants = []
    for tenant_id, data in tenant_info.tenants.items():
        tenant = data["tenant"]
        apartment = data["apartment"]
        rent = rent_records.get(tenant_id)

        if rent and rent.check_payment_status() == "overdue":
            overdue_tenants.append(tenant.display_info() + f"\nApartment: {apartment.display_details()}")

    return overdue_tenants


overdue_tenants = list_overdue_rent(tenant_info, rent_records)
for tenant in overdue_tenants:
    print(tenant)

print("\nMaintenance Requests:")
print(maintenance_request1.display_request())

policy1 = Policy(5, "No flowers on the balcony", "2024-09-03")
print("\nPolicy Compliance Check:", policy1.check_compliance(tenant1.lease_start_date))

#Problem 1:
#Implement an online movie library like Netflix. It should have users, admins that can add/remove content, subscriptions with trial period, movies.
#Every user should be able to add a movie in list of favourites.
#They should also be able to get a list of recommended movies (at least 3) (( Could be the last 3 added)).
#They should be able to mark movies as watched and also rate the movie with a rating ranging 1 to 5.
# Users should be able to get a list of all watched movies.
# Organize your code in modules and follow the good OOP principles.
# Start with designing your classes and entities in the project.
# **Tasks:**
# 1. Create the classes mentioned above, ensuring appropriate encapsulation and data validation where necessary.
# 2. Demonstrate the system's functionality by simulating interactions such as watching a movie,
# asking for recommendations, marking a movie as watched, rating a movie, listing all watched movies and so on.
# 3. Implement tests cases accordingly


class Movie:
    def __init__(self, title, genre, release_year, movie_id):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.movie_id = movie_id
        self.rating = None  # Rating will be assigned later

    def __str__(self):
        return f"Movie(title={self.title}, genre={self.genre}, year={self.release_year}, rating={self.rating})"

    def set_rating(self, rating):
        if 1 <= rating <= 10:
            self.rating = rating
        else:
            raise ValueError("Rating must be between 1 and 10.")

class User:
    def __init__(self, username, subscription):
        self.username = username
        self.subscription = subscription  # instance of Subscription class
        self.favourites = []
        self.watched_movies = []
        self.ratings = {}

    def add_to_favourites(self, movie):
        if movie not in self.favourites:
            self.favourites.append(movie)

    def mark_as_watched(self, movie):
        if movie not in self.watched_movies:
            self.watched_movies.append(movie)

    def rate_movie(self, movie, rating):
        if movie in self.watched_movies:
            movie.set_rating(rating)
            self.ratings[movie.movie_id] = rating
        else:
            print("Watch the movie in order to be able to rate it")

    def get_watched_movies(self):
        return self.watched_movies

    def get_favourite_movies(self):
        return self.favourites

    def get_recommendations(self, movie_library):
        return movie_library.get_latest_movies(2)

class Admin:
    def __init__(self, username):
        self.username = username

    def add_movie(self, movie_library, movie):
        movie_library.add_movie(movie)

    def remove_movie(self, movie_library, movie_id):
        movie_library.remove_movie(movie_id)

class Subscription:
    def __init__(self, user_type, trial_period_days=30):
        self.user_type = user_type  # 'free' or 'premium'
        self.trial_period_days = trial_period_days
        self.is_paid = False
        self.trial_expiry_date = None

    def activate_paid_subscription(self):
        self.is_paid = True
        self.user_type = 'TOTAL FULL MAX PRO'

    def is_trial_active(self):
        return self.trial_period_days > 0

class MovieGallery:
    def __init__(self):
        self.movies = {}

    def add_movie(self, movie):
        self.movies[movie.movie_id] = movie

    def remove_movie(self, movie_id):
        if movie_id in self.movies:
            del self.movies[movie_id]
        else:
            print("No such movie in gallery")

    def get_movie(self, movie_id):
        return self.movies.get(movie_id, None)

    def get_latest_movies(self, count):
        return list(self.movies.values())[-count:]

class Review:
    def __init__(self, movie, rating, review_text=""):
        self.movie = movie
        self.rating = rating
        self.review_text = review_text

movie_gallery = MovieGallery()

movie1 = Movie("TITANIC", "DRAMA", 1995, 1)
movie2 = Movie("TAXI", "Action", 2002, 2)
movie3 = Movie("Asterix and Obelix against Ceasar", "Comedy", 1992, 3)
movie4 = Movie("BORAT", "EDUCATIONAL", 2006, 4)

admin = Admin("admin1")
admin.add_movie(movie_gallery, movie1)
admin.add_movie(movie_gallery, movie2)
admin.add_movie(movie_gallery, movie3)
admin.add_movie(movie_gallery, movie4)

subscription = Subscription(user_type="free")
user = User(username="pesho_gleda", subscription=subscription)

user.add_to_favourites(movie1)
user.add_to_favourites(movie2)

user.mark_as_watched(movie1)

user.rate_movie(movie4, 10)

print("Watched Movies:")
for movie in user.get_watched_movies():
    print(movie)

print("\nFavourite Movies:")
for movie in user.get_favourite_movies():
    print(movie)

print("\nRecommendations:")
for movie in user.get_recommendations(movie_gallery):
    print(movie)