import matplotlib.pyplot as plt

def latex_to_png(latex_str, filename):
    fig, ax = plt.subplots()

    ax.text(0.5, 0.5, f"${latex_str}$", size=50, ha='center', va='center')
    ax.axis('off')

    plt.savefig(filename, format='png', bbox_inches='tight', pad_inches=0.4)
    plt.close(fig)
    
    return filename