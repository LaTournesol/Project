# Runs MDS on a provided distance matrix,
# returns a result containing the coordinates for the MDS graph
def scaling(adist, dim):
    mds = manifold.MDS(n_components=dim, dissimilarity="precomputed", random_state=4)
    results = mds.fit(adist)
    return adist, results

# Run MDS for n times on n random generated distance matrices,
# return a list of the GOF values from all the MDS fits.
def run_random_experiment(n):
    rand_result = []
    for i in range(0, n):
        adist = random_symmetric_matrix(32)
        adist, results = scaling(adist, 2)
        s = results.stress_
        rand_result.append(get_gof(s, adist))
    return rand_result

# Plot a gof_vs_dimension graph,
# dimension ranges from 1 to the dimension of the original matrix (32 in this case).
def gof_vs_dim(adist, max_dim):
    X = range(1, max_dim+1)
    Y = []
    for dim in range(1, max_dim+1):
        adist, results = scaling(adist, dim)
        s = results.stress_
        Y.append(get_gof(s, adist))

    plt.plot(X, Y, 'ro')
    plt.xlabel('Dimension')
    plt.ylabel('GOF')
    plt.show()

# Plot the MDS graph using the coordinates stored in the result returned from MDS process
def MDS_graph(coords):
    plt.subplots_adjust(bottom = 0.1)
    plt.scatter(
        coords[:, 0], coords[:, 1], marker = 'o'
        )
    for label, x, y in zip(teams, coords[:, 0], coords[:, 1]):
        plt.annotate(
            label,
            xy = (x, y), xytext = (-20, 20),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

    plt.show()

# Reconstruct a distance matrix using the coordinates returned from the MDS process
def reconstruct_distance_matrix(X, Y):
    D_2 = np.zeros((32, 32))
    for i in range(0, 32):
        this_pt = (X[i], Y[i])
        for j in range(0, 32):
            curr_pt = (X[j], Y[j])
            D_2[i][j] = pt_dist(this_pt, curr_pt)
    return D_2

# Return the distance of two points on a plane
def pt_dist(P1, P2):
    return math.sqrt(math.pow(P2[0] - P1[0], 2) + math.pow(P2[1] - P1[1], 2))

# Plot the difference between the original distance matrix and the reconstructed matrix after MDS
def D1_vs_D2(coords):
    X = coords[:, 0]
    Y = coords[:, 1]
    D_2 = reconstruct_distance_matrix(X, Y)

    plt.plot(adist, D_2, 'wo', range(0, 46), range(0, 46), 'k')
    plt.xlabel('Original Distance Matrix')
    plt.ylabel('Distance Matrix after MDS')
    plt.show()

# Returns the max, min, and mean from n number of random matrix experiment
def assess_random_experiment(list):
    max = 0
    min = 1
    sum = 0
    for gof in list:
        if gof > max:
            max = gof
        if gof < min:
            min = gof
        sum += gof
    mean = sum / len(list)
    return max, min, mean

adist, results = scaling(adist, 2)
coords = results.embedding_
s = results.stress_
# print get_gof(s, adist)
# gof_vs_dim(adist, 32)
# D1_vs_D2(coords)
MDS_graph(coords)