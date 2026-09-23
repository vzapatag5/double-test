from unittest.mock import Mock

from TicketPlus import TicketService
from InventarioStub import inventarioStub
from RepositorioFake import RepositorioFake
from UsuarioDummy import UsuarioDummy


def test_compra_exitosa():

    email_mock = Mock()

    service = TicketService(
        inventarioStub(),
        RepositorioFake(),
        email_mock
    )

    resultado = service.comprar(
        UsuarioDummy(),
        2
    )

    assert resultado is True

    email_mock.enviar_confirmacion.assert_called_once()
