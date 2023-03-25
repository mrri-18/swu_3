{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOQlxBqciCKS4roT6GqLK6D",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mrri-18/swu_3/blob/main/%EC%82%AC%EC%B9%99%EC%97%B0%EC%82%B0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bRBp2BXiX-dX",
        "outputId": "b41adfa8-61e9-417a-b421-70385fef1f55"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7 3\n",
            "10\n",
            "4\n",
            "21\n",
            "2\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "A,B=map(int,input().split()) #정수 2개를 입력 받아 연산결과를 출력\n",
        "print(A+B)\n",
        "print(A-B)\n",
        "print(A*B)\n",
        "print(int(A/B))\n",
        "print(A%B)"
      ]
    }
  ]
}