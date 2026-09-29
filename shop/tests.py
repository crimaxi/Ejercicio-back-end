from django.test import TestCase
from django.urls import reverse

from .models import Producto


class ListaProductosTests(TestCase):
	def test_muestra_productos_ordenados(self):
		Producto.objects.create(nombre="Zapatillas", codigo_barras="002", precio=2500, stock=3)
		Producto.objects.create(nombre="Camisa", codigo_barras="001", precio=1800, stock=5)

		response = self.client.get(reverse("productos"))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Camisa")
		self.assertContains(response, "Zapatillas")
		self.assertLess(response.content.index(b"Camisa"), response.content.index(b"Zapatillas"))

	def test_muestra_estado_vacio(self):
		response = self.client.get(reverse("productos"))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Todavía no hay productos registrados.")
