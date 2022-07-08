from abstract_class import ContaCorrente, ContaPoupanca

cp = ContaPoupanca(agencia=1111, conta=2222, saldo=0)
cp.depositar(10)
cp.sacar(8)

print('#########################')

cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.depositar(1000)
