#!/usr/bin/perl
use CGI qw(:standard);

print "Content-type:text/html\n\n";
print "<html>";
print "<title> Tic Tac Toe </title>";
print "<body>";
print "<form method=post name=f1 action=http://bonnevier.us/cgi-bin/ttt.cgi>";
print "Choice! <input type=text name=choice>";
print "</form>";



@board = (" ", " ", " ", " ", " ", " ", " ", " ", " ");

sub printBoard {

print "$board[0]<u>&nbsp &nbsp</u> \| $board[1]<u>&nbsp &nbsp</u> \|$board[2]<u>&nbsp &nbsp</u>\n </br>";
#print "--- \| ---\| --- \n</br>";
print "$board[3]<u>&nbsp &nbsp</u> \| $board[4]<u>&nbsp &nbsp</u> \|$board[5]<u>&nbsp &nbsp</u>\n </br>";
#print "--- \| ---\| ---\n</br>";
print "$board[6]&nbsp &nbsp \|$board[7]&nbsp &nbsp \|$board[8]&nbsp &nbsp \n </br>";
print "\n</br>";

}


sub rotateBoard {
	splice(@board, 0, 8, "$board[6]", "$board[3]", "$board[0]", "$board[7]", "$board[4]", "$board[1]",
	"$board[8]", "$board[5]", "$board[2]");
	}

sub choicePlayer {
		 $a = &param('choice');
		if ($board[$a] eq " ") 
			{		
			splice(@board, $a, 1, "X");
			}
		elsif ($board[$a] eq "X", "O") {			
		print "That square is taken-- Try Again!\n";
		}		
}



#Patterns to Check!
$gameover = 0;
$done = 0;
		
sub p1 {
if (($board[0] eq " ") and ($board[1] eq "O") and ($board[2] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
}
rotateBoard();
if (($board[0] eq " ") and ($board[1] eq "O") and ($board[2] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[1] eq "O") and ($board[2] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[1] eq "O") and ($board[2] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p2 {
if (($board[0] eq " ") and ($board[3] eq "O") and ($board[6] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[3] eq "O") and ($board[6] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[3] eq "O") and ($board[6] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[3] eq "O") and ($board[6] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p3 {
if (($board[0] eq " ") and ($board[4] eq "O") and ($board[8] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[4] eq "O") and ($board[8] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[4] eq "O") and ($board[8] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[4] eq "O") and ($board[8] eq "O") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p4{
if (($board[1] eq " ") and ($board[0] eq "O") and ($board[2] eq "O") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[0] eq "O") and ($board[2] eq "O") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[0] eq "O") and ($board[2] eq "O") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[0] eq "O") and ($board[2] eq "O") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
}	

sub p5 {
if (($board[1] eq " ") and ($board[4] eq "O") and ($board[7] eq "O") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[4] eq "O") and ($board[7] eq "O") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[4] eq "O") and ($board[7] eq "O") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[4] eq "O") and ($board[7] eq "O") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p6 {
if (($board[4] eq " ") and ($board[1] eq "O") and ($board[7] eq "O") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[1] eq "O") and ($board[7] eq "O") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[1] eq "O") and ($board[7] eq "O") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[1] eq "O") and ($board[7] eq "O") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p7 {
if (($board[4] eq " ") and ($board[0] eq "O") and ($board[8] eq "O") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[0] eq "O") and ($board[8] eq "O") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[0] eq "O") and ($board[8] eq "O") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[0] eq "O") and ($board[8] eq "O") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p8 {
if (($board[0] eq " ") and ($board[1] eq "X") and ($board[2] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;	
	}
rotateBoard();
if (($board[0] eq " ") and ($board[1] eq "X") and ($board[2] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;	
	}
rotateBoard();
if (($board[0] eq " ") and ($board[1] eq "X") and ($board[2] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;	
	}
rotateBoard();
if (($board[0] eq " ") and ($board[1] eq "X") and ($board[2] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;	
	}
rotateBoard();
}

sub p9 {
if (($board[0] eq " ") and ($board[3] eq "X") and ($board[6] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}	 
rotateBoard();
if (($board[0] eq " ") and ($board[3] eq "X") and ($board[6] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}	 
rotateBoard();
if (($board[0] eq " ") and ($board[3] eq "X") and ($board[6] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}	 
rotateBoard();
if (($board[0] eq " ") and ($board[3] eq "X") and ($board[6] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}	 
rotateBoard();
}

sub p10 {
if (($board[0] eq " ") and ($board[4] eq "X") and ($board[8] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[4] eq "X") and ($board[8] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[4] eq "X") and ($board[8] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[4] eq "X") and ($board[8] eq "X") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p11 {
if (($board[1] eq " ") and ($board[0] eq "X") and ($board[2] eq "X") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[0] eq "X") and ($board[2] eq "X") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[0] eq "X") and ($board[2] eq "X") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[0] eq "X") and ($board[2] eq "X") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p12 {
if (($board[1] eq " ") and ($board[4] eq "X") and ($board[7] eq "X") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[4] eq "X") and ($board[7] eq "X") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[4] eq "X") and ($board[7] eq "X") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[4] eq "X") and ($board[7] eq "X") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p13 {
if (($board[4] eq " ") and ($board[1] eq "X") and ($board[7] eq "X") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[1] eq "X") and ($board[7] eq "X") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[1] eq "X") and ($board[7] eq "X") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[1] eq "X") and ($board[7] eq "X") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p14 {
if (($board[4] eq " ") and ($board[0] eq "X") and ($board[8] eq "X") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[0] eq "X") and ($board[8] eq "X") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[0] eq "X") and ($board[8] eq "X") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($board[0] eq "X") and ($board[8] eq "X") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p15 {
if (($board[1] eq " ") and ($board[2] eq "X") and ($board[6] eq "X") and ($board[4] eq "O") and
	($board[0] eq " ") and ($board[3] eq " ") and ($board[5] eq " ") and ($board[7] eq " ") and ($board[8] eq " ")
	and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[2] eq "X") and ($board[6] eq "X") and ($board[4] eq "O") and
	($board[0] eq " ") and ($board[3] eq " ") and ($board[5] eq " ") and ($board[7] eq " ") and ($board[8] eq " ")
	and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[2] eq "X") and ($board[6] eq "X") and ($board[4] eq "O") and
	($board[0] eq " ") and ($board[3] eq " ") and ($board[5] eq " ") and ($board[7] eq " ") and ($board[8] eq " ")
	and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[2] eq "X") and ($board[6] eq "X") and ($board[4] eq "O") and
	($board[0] eq " ") and ($board[3] eq " ") and ($board[5] eq " ") and ($board[7] eq " ") and ($board[8] eq " ")
	and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p16 {
if (($board[0] eq " ") and ($board[1] eq "X") and ($board[3] eq "X") and ($board[4] eq "O") and ($board[2] eq " ")
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[1] eq "X") and ($board[3] eq "X") and ($board[4] eq "O") and ($board[2] eq " ")
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[1] eq "X") and ($board[3] eq "X") and ($board[4] eq "O") and ($board[2] eq " ")
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[1] eq "X") and ($board[3] eq "X") and ($board[4] eq "O") and ($board[2] eq " ")
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p17 {
if (($board[0] eq " ") and ($board[2] eq "X" ) and ($board[3] eq "X") and ($board[4] eq "O") and ($board[1] eq " ") 
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[2] eq "X" ) and ($board[3] eq "X") and ($board[4] eq "O") and ($board[1] eq " ") 
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[2] eq "X" ) and ($board[3] eq "X") and ($board[4] eq "O") and ($board[1] eq " ") 
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[2] eq "X" ) and ($board[3] eq "X") and ($board[4] eq "O") and ($board[1] eq " ") 
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p18 {
if (($board[8] eq " ") and ($board[2] eq "X") and ($board[7] eq "X") and ($board[4] eq "O") and ($board[5] eq " ") 
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 8, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[8] eq " ") and ($board[2] eq "X") and ($board[7] eq "X") and ($board[4] eq "O") and ($board[5] eq " ") 
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 8, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[8] eq " ") and ($board[2] eq "X") and ($board[7] eq "X") and ($board[4] eq "O") and ($board[5] eq " ") 
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 8, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[8] eq " ") and ($board[2] eq "X") and ($board[7] eq "X") and ($board[4] eq "O") and ($board[5] eq " ") 
	and ($board[6] eq " ") and ($done == 0))
	{
	splice(@board, 8, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p19 {
if (($board[0] eq " ") and ($board[2] eq "X") and ($board[6] eq "X") and ($board[4] eq "O") and ($board[5] eq " ") 
	and ($board[7] eq " ") and ($board[8] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[2] eq "X") and ($board[6] eq "X") and ($board[4] eq "O") and ($board[5] eq " ") 
	and ($board[7] eq " ") and ($board[8] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[2] eq "X") and ($board[6] eq "X") and ($board[4] eq "O") and ($board[5] eq " ") 
	and ($board[7] eq " ") and ($board[8] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[2] eq "X") and ($board[6] eq "X") and ($board[4] eq "O") and ($board[5] eq " ") 
	and ($board[7] eq " ") and ($board[8] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p20 {
if (($board[0] eq " ") and ($board[4] eq "X") and ($board[8] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[4] eq "X") and ($board[8] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[4] eq "X") and ($board[8] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($board[4] eq "X") and ($board[8] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p21 {
if (($board[1] eq " ") and ($board[4] eq "X") and ($board[7] eq " ") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done =1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[4] eq "X") and ($board[7] eq " ") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done =1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[4] eq "X") and ($board[7] eq " ") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done =1;
	}
rotateBoard();
if (($board[1] eq " ") and ($board[4] eq "X") and ($board[7] eq " ") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done =1;
	}
rotateBoard();
}

sub p22 {
if (($board[4] eq " ") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[4] eq " ") and ($done == 0))
	{
	splice(@board, 4, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p23 {
if (($board[0] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
if (($board[0] eq " ") and ($done == 0))
	{
	splice(@board, 0, 1, "O");
	$done = 1;
	}
rotateBoard();
}

sub p24 {
if (($board[1] eq " ") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done =1 ;
	}
rotateBoard();
if (($board[1] eq " ") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done =1 ;
	}
rotateBoard();
if (($board[1] eq " ") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done =1 ;
	}
rotateBoard();
if (($board[1] eq " ") and ($done == 0))
	{
	splice(@board, 1, 1, "O");
	$done =1 ;
	}
rotateBoard();
}

sub win1 {
if (($board[0] eq "O") and ($board[1] eq "O") and ($board[2] eq "O") and ($gameover == 0))
	{
	print "Computer Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "O") and ($board[1] eq "O") and ($board[2] eq "O") and ($gameover == 0))
	{
	print "Computer Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "O") and ($board[1] eq "O") and ($board[2] eq "O") and ($gameover == 0))
	{
	print "Computer Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "O") and ($board[1] eq "O") and ($board[2] eq "O") and ($gameover == 0))
	{
	print "Computer Wins!\n";
	$gameover = 1;
	}
rotateBoard();
}

sub win2 {
if (($board[0] eq "O") and ($board[4] eq "O") and ($board[8] eq "O") and ($gameover == 0))
	{
	print "Computer Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "O") and ($board[4] eq "O") and ($board[8] eq "O") and ($gameover == 0))
	{
	print "Computer Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "O") and ($board[4] eq "O") and ($board[8] eq "O") and ($gameover == 0))
	{
	print "Computer Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "O") and ($board[4] eq "O") and ($board[8] eq "O") and ($gameover == 0))
	{
	print "Computer Wins!\n";
	$gameover = 1;
	}
rotateBoard();
}

sub win3 {
if (($board[0] eq "X") and ($board[1] eq "X") and ($board[2] eq "X") and ($gameover == 0))
	{
	print "Human Being Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "X") and ($board[1] eq "X") and ($board[2] eq "X") and ($gameover == 0))
	{
	print "Human Being Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "X") and ($board[1] eq "X") and ($board[2] eq "X") and ($gameover == 0))
	{
	print "Human Being Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "X") and ($board[1] eq "X") and ($board[2] eq "X") and ($gameover == 0))
	{
	print "Human Being Wins!\n";
	$gameover = 1;
	}
rotateBoard();
}

sub win4 {
if (($board[0] eq "X") and ($board[4] eq "X") and ($board[8] eq "X") and ($gameover == 0))
	{
	print "Human Being Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "X") and ($board[4] eq "X") and ($board[8] eq "X") and ($gameover == 0))
	{
	print "Human Being Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "X") and ($board[4] eq "X") and ($board[8] eq "X") and ($gameover == 0))
	{
	print "Human Being Wins!\n";
	$gameover = 1;
	}
rotateBoard();
if (($board[0] eq "X") and ($board[4] eq "X") and ($board[8] eq "X") and ($gameover == 0))
	{
	print "Human Being Wins!\n";
	$gameover = 1;
	}
rotateBoard();
}

sub draw {

if (($board[0] ne " ") and ($board[1] ne " ") and ($board[2] ne " ") and ($board[3] ne " ") and ($board[4] ne " ")
	and ($board[5] ne " ") and ($board[6] ne " ") and ($board[7] ne " ") and ($board[8] ne " ") and $gameover == 0)
	{
	print "It is all over!!!!!! No one wins!!!!\n";
	$gameover = 1;
	}
}

# End of Pattern Checking


sub Turn {

printBoard();
print "---------------------\n";
print "---------------------\n";
print "Please choose a square 0 through 8!\n";
print "The squares are labeled beginning with the top left (0)
	and moving to the bottom right (8)\n";
choicePlayer();

p1();
p2();
p3();
p4();
p5();
p6();
p7();
p8();
p9();
p10();
p11();
p12();
p13();
p14();
p15();
p16();
p17();
p18();
p19();
p20();
p21();
p22();
p23();
p24();
win1();
win2();
win3();
win4();
draw();
$done = 0;
}

while ($gameover == 0) {
Turn();
}

