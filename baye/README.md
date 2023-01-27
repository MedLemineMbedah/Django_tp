1-activer votre environnement avec `venv\Scripts\activate` sous windows, sous Mac/Linux:```source venv/bin/activate```
2-Lancer ces commandes respectivement :
	// NB: Selon la version de python(Tu peux utiliser:py, python ou python3) 
	a-`python3 manage.py makemigrations`  
	b-`python3 manage.py migrate`
	c-lancer votre server `python3 manage.py runserver`
	
3-Pour ajouter les données aux models:
	a-python3 manage.py shell
	b-from baye_tache.models import Book
		1-pour ajouter 1 objet :
			book = Book(book_id='py',book_title='Python')
			book.save()
			print(book.book_title)
			from baye_tache.models import Reviews
			Reviws_list = [{'review_id': 'review1', 'review_text': 'best book','review_sentument':'review_sentument','book':book},
				       {'review_id': 'review1', 'review_text': 'best book','review_sentument':'review_sentument','book':book},
				       {'review_id': 'review3', 'review_text': 'bad book','review_sentument':'review_sentument','book':book}]
			for review in Reviws_list:
    			   r = Reviews(review_id=review['review_id'], review_text=review['review_text'], review_sentument=review['review_sentument'], book=review['book'])
   			   r.save()			
		2-pour ajouter une list des objets :
			-Methode1:
				book_list = [{'book_id': 'id1', 'book_title': 'title1'}, {'book_id': 'id2', 'book_title': 'title2'}, {'book_id': 'id3', 'book_title': 'title3'}]
				book_objs = [Book(**book) for book in book_list]
				Book.objects.bulk_create(book_objs)
			
			-Methode2:
				book_list = [{'book_id': 'id1', 'book_title': 'title1'}, {'book_id': 'id2', 'book_title': 'title2'}, {'book_id': 'id3', 'book_title': 'title3'}]
				for book in book_list:
    					b = Book(book_id=book['book_id'], book_title=book['book_title'])
    					b.save()
    		3-Pour supprimer : Book.objects.all().delete()
					

# Reviws_list = [{'review_id': 'r1', 'review_text': 'best book','review_sentument':'review_sentument','book':book1},{'review_id': 'r2', 'review_text': 'grate book','review_sentument':'review_sentument','book':book1},{'review_id': 'review3', 'review_text': 'bad book','review_sentument':'review_sentument','book':book1}]
# for review in Reviws_list:
#     r = Reviews(review_id=review['review_id'], review_text=review['review_text'], review_sentument=review['review_sentument'], book=review['book'])
#     r.save()	

	
	
