import matplotlib.pyplot as plt


def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()


def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))
    names_lst = ['Image{}'.format(i) for i in ranger(1, number_images)]
    names_lst.append("Result")
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()


def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=true, sharey=true)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} histogram'.format(color_lst.title()))
        ax.hist(image[:, :, index].rave(), bins=256, color=color, alpha=0.8)
    fig.tight_layout()
    plt_show()