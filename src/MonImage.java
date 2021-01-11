import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

//http://remy-manu.no-ip.biz/Java/Tutoriels/AWT/TraitementImages.html

public class MonImage {

    private String lien;
    private BufferedImage img;

    public MonImage()
    {

    }
    public MonImage(String lien) throws IOException
    {
        this.lien = lien;
        img = ImageIO.read(new File(this.lien));
    }


    public MonImage seuillage(int seuil)
    {
        MonImage monImageSeuil = this;

        for (int i=0; i<this.img.getWidth(); i++)
        {
            for (int j=0; j<this.img.getHeight(); j++)
            {
                    if(this.img.getRGB(i,j)<seuil)
                    {
                        monImageSeuil.img.setRGB(i, j, 0);
                    }
                    else
                    {
                        monImageSeuil.img.setRGB(i, j, 255);
                    }
            }
        }
        for(int i=0; i< img.getWidth(); i++)
        {
            for(int j=0; j< img.getHeight(); j++)
            {
                System.out.println(img.getRGB(i, j)+" - ");
            }
            System.out.println();
        }

        return monImageSeuil;
    }

    public MonImage addition(MonImage img)
    {

        MonImage monImageBase = this;
        MonImage res = this;

        for(int i = 0; i< monImageBase.img.getWidth(); i++)
        {
            for(int j = 0; j< monImageBase.img.getHeight(); j++)
            {
                int color = monImageBase.img.getRGB(i,j)+img.img.getRGB(i,j);

                if(color>255)
                {
                    color=255;
                }

                res.img.setRGB(i,j,color);
            }
        }
        return res;
    }

    public MonImage soustraction(MonImage img)
    {

        MonImage monImageBase = this;
        MonImage res = this;

        for(int i = 0; i< monImageBase.img.getWidth(); i++)
        {
            for(int j = 0; j< monImageBase.img.getHeight(); j++)
            {
                int color = monImageBase.img.getRGB(i,j)-img.img.getRGB(i,j);

                if(color<0)
                {
                    color=0;
                }

                res.img.setRGB(i,j,color);
            }
        }
        return res;
    }

    public MonImage erosion()
    {
        MonImage erodee = this;
        MonImage binaire = this.seuillage(120);
        for (int i=1; i<=binaire.img.getWidth()-2; i++)
        {
            for (int j=1; j<=binaire.img.getHeight()-2; j++)
            {
                int somme = 0;
                for(int k=-1; k<=1; k++)
                {
                    for(int l=-1; l<=1; l++)
                    {
                        somme += binaire.img.getRGB(i+k, j-l);
                    }
                }

                if(somme == 2295)
                {
                    erodee.img.setRGB(i, j, 255);
                }
                else
                {
                    erodee.img.setRGB(i, j, 0);
                }
            }
        }

        return erodee;
    }

    public MonImage dilatation()
    {
        MonImage dilatee = this;
        MonImage binaire = this.seuillage(120);
        for (int i=1; i<=binaire.img.getWidth()-2; i++)
        {
            for (int j=1; j<=binaire.img.getHeight()-2; j++)
            {
                int somme = 0;
                for(int k=-1; k<=1; k++)
                {
                    for(int l=-1; l<=1; l++)
                    {
                        somme += binaire.img.getRGB(i+k, j-l);
                    }
                }

                if(somme == 0)
                {
                    dilatee.img.setRGB(i, j, 0);
                }
                else
                {
                    dilatee.img.setRGB(i, j, 255);
                }
            }
        }

        return dilatee;
    }

    public MonImage ouverture()
    {
        MonImage erodee = this.erosion();
        MonImage result = erodee.dilatation();
        return result;
    }

    public MonImage fermeture()
    {
        MonImage dilatee = this.dilatation();
        MonImage result = dilatee.erosion();
        return result;
    }

    //ajouter un paramètre L
    public MonImage transformationDeVoisinage()
    {
        return null;
    }

    public MonImage amincissement()
    {
        return null;
    }

    public MonImage epaississement()
    {
        return null;
    }



    public BufferedImage getImg() {
        return img;
    }
    public void setImg(BufferedImage img) {
        this.img = img;
    }


}
