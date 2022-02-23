def generate_data(n_samples=20, n_feats=2):
  """ Generates simulated data.

  Args:
      n_samples (int): observed students.
      n_feats (int): number of features characterizing each student.
      n_groups (int): number of groups (clusters).

  Returns:
      x (ndarray): the features (inputs).
  """
  # We fix the seed to our random number generator to ensure that
  # we always get the same psuedo-random number sequence.
  np.random.seed(121)

  # Sample features for n_samples students, distributed 
  # around n_groups centers.
  x, _ = dataset.make_blobs(n_samples=n_samples-2, 
                            n_features=n_feats, 
                            centers=[[9,21],[9, 12],[20,15],[20,8]],
                            cluster_std=[[2,1], [1,1], [2,1], [2,1]],
                            center_box = (5, 25))
  # add two extra students to better emphasize our findings
  x = np.append(x, [[1, 5], [15, 1]], axis=0)
  return x
