import psycopg2 
import numpy as np 

class BinarizeArray(object):


	def adapt_array(self, a):
		return psycopg2.Binary(a)



	def typecast_array(self, data, cur):
		if data is None: return None
		buf = psycopg2.BINARY(data, cur)
		return np.frombuffer(buf)


	def run(self):
		psycopg2.extensions.register_adapter(np.ndarray, self.adapt_array)
		ARRAY = psycopg2.extensions.new_type(psycopg2.BINARY.values,
	'ARRAY', self.typecast_array)
		psycopg2.extensions.register_type(ARRAY)
