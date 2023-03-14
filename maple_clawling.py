{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "\n",
    "import pandas as pd\n",
    "from html_table_parser import parser_functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = []\n",
    "for i in list(range(2126,2064,-1)):\n",
    "    url = 'https://www.gamemeca.com/ranking.php?rid=' + str(i)\n",
    "    request = requests.get(url)\n",
    "    soup = BeautifulSoup(request.text,'html.parser')\n",
    "    \n",
    "    rnk = soup.find('table',{'class' :'ranking-table'})\n",
    "    rank_cr = rnk.find_all(class_ = 'rank')\n",
    "    rank_list = []\n",
    "    for j in rank_cr:\n",
    "        rank = int(j.get_text())\n",
    "        rank_list.append(rank)\n",
    "    links = rnk.find_all('a')\n",
    "    title_list =[]\n",
    "    for k in links:\n",
    "        if len(k) !=0 and 'gmview' in k.attrs['href']:\n",
    "            title = k.get_text()\n",
    "            title_list.append(title)\n",
    "    if len(data) ==0:\n",
    "        data = pd.concat([pd.DataFrame(rank_list),pd.DataFrame(title_list)],axis = 1)\n",
    "        data['probability'] = i\n",
    "    else:\n",
    "        new_data = pd.concat([pd.DataFrame(rank_list),pd.DataFrame(title_list)],axis = 1)\n",
    "        new_data['probability'] = i\n",
    "        data = pd.concat([data,new_data],axis=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "data.columns = ['rank','title','prob']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "maple = data[data['title'] =='메이플스토리']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "maple.to_csv('C:/Users/82106/Desktop/nc_data/maple.csv',encoding ='utf-8-sig')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "hide_input": false,
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
