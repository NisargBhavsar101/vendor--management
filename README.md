					Vendor-Management Assignment
Project Setup:
	•	Clone the Repository:
		o	https://github.com/NisargBhavsar101/vendor-management.git
		o	cd vendor-management
	•	Apply Database Migrations (Commands):
		o	python manage.py makemigrations
		o	python manage.py sqlmigrate vendor_api 0001_initial
		o	python manage.py migrate
	•	Create Superuser (for admin access):
		o	python manage.py createsuperuser
	•	Run Development Server:
		o	python manage.py runserver
	•	Access Admin Panel:
	Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
Overview:
	The Vendor Management System is built using Django REST Framework. It manages vendor profiles, purchase orders.
Key Features:
	Vendor Profile Management:
		Create, list, retrieve, update, and delete vendors using API endpoints.
	Purchase Order Tracking:
		Create, list, retrieve, update, and delete purchase orders.
	Vendor Performance Evaluation:
		Performance metrics include on-time delivery rate, quality rating average, average response time, and fulfillment rate.
	Data Models:
		Vendor Model: Stores vendor information.
		Purchase Order Model: Captures details of each purchase order.
	Historical Performance Model: Optionally stores historical data for trend analysis.

Api Endpoints:
	Vendor Profile Management:
		Create Vendor:
			POST /api/vendors/
		List Vendors:
			GET /api/vendors/
		Retrieve Vendor:
			GET /api/vendors/{vendor_id}/
		Update Vendor:
			PUT /api/vendors/{vendor_id}/
		Delete Vendor:
			DELETE /api/vendors/{vendor_id}
	Purchase Order Tracking:
		Create Purchase Order:
			POST /api/purchase_orders/
		List Purchase Orders:
			GET /api/purchase_orders/
		Retrieve Purchase Order:
			GET /api/purchase_orders/{po_id}/
		Update Purchase Order:
			PUT /api/purchase_orders/{po_id}/
		Delete Purchase Order:
			DELETE /api/purchase_orders/{po_id}/
Conclusion:
	The Vendor Management System API provides a simple way to manage vendors, track purchase orders, and evaluate vendor performance. You can create, update, and delete 			vendors, as well as create, update, and acknowledge purchase orders.


