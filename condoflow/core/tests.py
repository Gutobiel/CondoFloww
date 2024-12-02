""" from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.contrib.auth.models import User
from core.models import Profile
import json

class ReuniaoTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Cria usuários de teste
        funcionario1 = User.objects.create_user(username='funcionario1', email='funcionario1@example.com', password='password')
        Profile.objects.create(user=funcionario1, user_type='F')
        
        morador1 = User.objects.create_user(username='morador1', email='morador1@example.com', password='password')
        Profile.objects.create(user=morador1, user_type='M')
        
        morador2 = User.objects.create_user(username='morador2', email='morador2@example.com', password='password')
        Profile.objects.create(user=morador2, user_type='M')

    def test_enviar_reuniao_para_funcionarios(self):
        data = {
            'assunto': 'Reunião de Teste',
            'local': 'Sala de Reuniões',
            'data': '2023-10-10T10:00',
            'urgencia': 'alta',
            'descricao': 'Discussão sobre o projeto X',
            'mensagem': 'Por favor, compareçam.',
            'destinatarios': 'funcionarios'
        }
        response = self.client.post(
            reverse('enviar_reuniao'),
            data=json.dumps(data),
            content_type='application/json'
        )

        # Verifica se a resposta foi bem-sucedida
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

        # Verifica se o e-mail foi enviado
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Reunião de Teste')
        self.assertIn('Sala de Reuniões', mail.outbox[0].body)
        self.assertIn('Discussão sobre o projeto X', mail.outbox[0].body)
        self.assertIn('Por favor, compareçam.', mail.outbox[0].body)
        self.assertIn('funcionario1@example.com', mail.outbox[0].to)
        self.assertNotIn('morador1@example.com', mail.outbox[0].to)
        self.assertNotIn('morador2@example.com', mail.outbox[0].to)

    def test_enviar_reuniao_para_moradores(self):
        data = {
            'assunto': 'Reunião de Teste',
            'local': 'Sala de Reuniões',
            'data': '2023-10-10T10:00',
            'urgencia': 'alta',
            'descricao': 'Discussão sobre o projeto X',
            'mensagem': 'Por favor, compareçam.',
            'destinatarios': 'moradores'
        }
        response = self.client.post(
            reverse('enviar_reuniao'),
            data=json.dumps(data),
            content_type='application/json'
        )

        # Verifica se a resposta foi bem-sucedida
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

        # Verifica se o e-mail foi enviado
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Reunião de Teste')
        self.assertIn('Sala de Reuniões', mail.outbox[0].body)
        self.assertIn('Discussão sobre o projeto X', mail.outbox[0].body)
        self.assertIn('Por favor, compareçam.', mail.outbox[0].body)
        self.assertNotIn('funcionario1@example.com', mail.outbox[0].to)
        self.assertIn('morador1@example.com', mail.outbox[0].to)
        self.assertIn('morador2@example.com', mail.outbox[0].to)

    def test_enviar_reuniao_para_todos(self):
        data = {
            'assunto': 'Reunião de Teste',
            'local': 'Sala de Reuniões',
            'data': '2023-10-10T10:00',
            'urgencia': 'alta',
            'descricao': 'Discussão sobre o projeto X',
            'mensagem': 'Por favor, compareçam.',
            'destinatarios': 'todos'
        }
        response = self.client.post(
            reverse('enviar_reuniao'),
            data=json.dumps(data),
            content_type='application/json'
        )

        # Verifica se a resposta foi bem-sucedida
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

        # Verifica se o e-mail foi enviado
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Reunião de Teste')
        self.assertIn('Sala de Reuniões', mail.outbox[0].body)
        self.assertIn('Discussão sobre o projeto X', mail.outbox[0].body)
        self.assertIn('Por favor, compareçam.', mail.outbox[0].body)
        self.assertIn('funcionario1@example.com', mail.outbox[0].to)
        self.assertIn('morador1@example.com', mail.outbox[0].to)
        self.assertIn('morador2@example.com', mail.outbox[0].to) """