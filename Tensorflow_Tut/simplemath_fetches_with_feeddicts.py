import tensorflow as tf

W = tf.constant([10,100], name='constant_W')

x = tf.placeholder(tf.int32, name='x')
b = tf.placeholder(tf.int32, name='b')

Wx = tf.multiply(W,x,name='Wx')

y = tf.add(Wx,b,name='y')

y_ = tf.subtract(x,b,name='y_')

with tf.Session() as sess:
	print 'intermediate result Wx = ', sess.run(Wx, feed_dict={x: [3,33]})

	print 'final result: Wx + b = ', sess.run(y, feed_dict={x: [5,50], b: [7,9]})

	print 'intermediate specified: Wx + b = ', sess.run(fetches=y, feed_dict={Wx:[100,1000], b: [7,9]})

	print 'two results: [Wx + b, x - b] = ',sess.run(fetches=[y,y_], feed_dict={x:[5,50], b: [7,9]})

writer = tf.summary.FileWriter('.', sess.graph)
writer.close()
