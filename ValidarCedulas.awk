#!/bin/awk -f

#BEGIN
BEGIN{
	FS = "";
}

#Middle
{
	suma = 0;

	for(i=1;i<10;i++)
	{

		if ( i%2 != 0  )
		{

			if ( $i*2 >= 10 )
			{
				suma = suma + ($i*2 - 9);
			}
			else
			{
				suma = suma + $i*2;
			}
		}
		else
		{
			suma = suma + $i;

		}
	}

	#Comprobacion del ultimo digito
	DecSup = (int(suma/10) + 1) * 10;
	LastDigit = DecSup - suma;

	if ( LastDigit == 10 )
	{
		LastDigit = 0;
	}

	if (LastDigit == $10)
	{
		print $0
	}
	else
	{
		print "" 
	}

}
#End
END{
	sort "ParVal.txt"
}
