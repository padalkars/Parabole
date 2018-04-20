import logging
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

#Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files
'''
def suitable_clusters(documents):
	from scipy.spatial.distance import cdist, pdist
	from sklearn.cluster import KMeans

	K = range(1,50)
	KM = [KMeans(n_clusters=k).fit(documents) for k in K]
	centroids = [k.cluster_centers_ for k in KM]

	D_k = [cdist(documents, cent, 'euclidean') for cent in centroids]
	cIdx = [np.argmin(D,axis=1) for D in D_k]
	dist = [np.min(D,axis=1) for D in D_k]
	avgWithinSS = [sum(d)/dt_trans.shape[0] for d in dist]

	# Total with-in sum of square
	wcss = [sum(d**2) for d in dist]
	tss = sum(pdist(dt_trans)**2)/dt_trans.shape[0]
	bss = tss-wcss

	kIdx = 10-1
	
	# elbow curve
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(K, avgWithinSS, 'b*-')
	ax.plot(K[kIdx], avgWithinSS[kIdx], marker='o', markersize=12, 
	markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
	plt.grid(True)
	plt.xlabel('Number of clusters')
	plt.ylabel('Average within-cluster sum of squares')
	plt.title('Elbow for KMeans clustering')

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(K, bss/tss*100, 'b*-')
	plt.grid(True)
	plt.xlabel('Number of clusters')
	plt.ylabel('Percentage of variance explained')
	plt.title('Elbow for KMeans clustering')

'''
def km(documents,name):
	mypath_output = "output"
	fh = open(os.path.join(mypath_output,name),"w")
		
	vectorizer = TfidfVectorizer(stop_words='english')
	X = vectorizer.fit_transform(documents)
	true_k = 3

	model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
	model.fit(X)

	print("Top terms per cluster:")
	
	#Co-ordinates of the cluster center
	order_centroids = model.cluster_centers_.argsort()[:, ::-1] 
	terms = vectorizer.get_feature_names()
	for i in range(true_k):
		print("Cluster %d:" % i)
		for ind in order_centroids[i, :10]:		#10 represents number of words per cluster
			print(' %s' % terms[ind])
			fh.write(terms[ind] + ' ')
		fh.write('\n')
		print

	print("\n")
	#print("Prediction")

#Function you will be working with


def creating_subclusters(list_of_terms, name_of_file):
	#global documents
	documents = [] 
    # Your code that converts the cluster into subclusters and saves the output in the output folder with the same name as input file
    #Note the writing to file has to be handled by you.
	mypath_input = "input"
	with open(os.path.join(mypath_input,name_of_file), "r") as f:
		l = f.read()
		for line in l.split(' '):
			documents.append(line)
	#print(documents)
	km(documents,name_of_file)
    #pass
	
#Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
	
    #Folder where the input files are present
    mypath = "input"
    list_of_input_files = read_directory(mypath)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath,each_file), "r") as f:
            file_contents = f.read()
        list_of_term_in_cluster = file_contents.split()

        # Sending the terms to be converted to subclusters in your code
        creating_subclusters(list_of_term_in_cluster, each_file)


#End of code
