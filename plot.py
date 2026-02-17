import numpy as np
import matplotlib.pyplot as plt

categorias = [
    'Resistência à Tração', 
    'Rigidez (Módulo)', 
    'Resistência Térmica', 
    'Facilidade de Impressão', 
    'Estabilidade Dimensional',
    'Resistência ao Impacto'
]
num_vars = len(categorias)


dados_abs = [2, 2, 2, 5, 3, 4]
dados_pa12_cf = [4, 5, 4, 3, 5, 4]
dados_pa6_cf = [5, 3, 5, 2, 2, 4]

angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angulos += angulos[:1]
dados_abs += dados_abs[:1]
dados_pa12_cf += dados_pa12_cf[:1]
dados_pa6_cf += dados_pa6_cf[:1]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

ax.plot(angulos, dados_abs, color='#1f77b4', linewidth=2, label='ABS', marker='o')
ax.fill(angulos, dados_abs, color='#1f77b4', alpha=0.1)
ax.plot(angulos, dados_pa12_cf, color='#ff7f0e', linewidth=2, label='PA12-CF', marker='o')
ax.fill(angulos, dados_pa12_cf, color='#ff7f0e', alpha=0.1)
ax.plot(angulos, dados_pa6_cf, color='#2ca02c', linewidth=2, label='PA6-CF', marker='o')
ax.fill(angulos, dados_pa6_cf, color='#2ca02c', alpha=0.1)

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angulos[:-1], categorias, color='black', size=11)
ax.set_rlabel_position(30)
plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=9)
plt.ylim(0, 5)

plt.title('Comparativo Técnico: ABS vs PA12-CF vs PA6-CF', size=16, pad=30, fontweight='bold')
plt.legend(loc='upper left', bbox_to_anchor=(1.15, 1.05), fontsize=10)

plt.savefig('comparativo_final_materiais.png', dpi=300, bbox_inches='tight')
plt.show()
