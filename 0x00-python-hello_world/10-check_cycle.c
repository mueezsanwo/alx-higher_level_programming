#include "lists.h"
#include <stdlib.h>

/**
*check_cycle - to checks if a singly linked list has a cycle in it.
*@list: a singly linked list.
*Return: 0 if it is not a cycle, 1 if it is a cycle.
*/
int check_cycle(listint_t *list)
{
	listint_t  *a, *b;

	if (list == NULL || list->next == NULL)
		return (0);
	a = list->next;
	b = list->next->next;

	while (a && b && b->next)
	{
		if (a == b)
			return (1);
		a = a->next;
		b = b->next->next;
	}
	return (0);
}
