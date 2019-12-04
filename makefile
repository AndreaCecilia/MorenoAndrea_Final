resultado.png: data.dat Graficas_3.py
	python Graficas_3.py
    
data.dat : evolve.x
	./evolve.x > data.dat

evolve.x : c.cpp
	c++ c.cpp -o evolve.x

clean:
	rm evolve.x *.dat