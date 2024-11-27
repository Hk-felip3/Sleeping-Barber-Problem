# Sleeping-Barber-Problem
This problem models a system where a barber serves customers. Se não houver 
clientes, ele dorme; caso contrário, atende um cliente de cada vez. O problema 
ilustra a gestão de recursos limitados (cadeiras) e o controle de sincronização 
entre threads.

Funcionamento:

Um semáforo é usado para sinalizar quando clientes chegam.

O barbeiro aguarda a chegada de clientes e corta o cabelo de um por vez.

Se não houver cadeiras disponíveis, clientes extras vão embora.

Este é um exemplo clássico de sincronização que usa semáforos para coordenar threads.
