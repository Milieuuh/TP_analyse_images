import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.image.ImageView;
import javafx.scene.image.Image;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.awt.image.BufferedImage;
import java.io.File;
import java.net.URL;

public class fenetre extends Parent {

   // BufferedImage image;

    public fenetre(Stage primaryStage)
    {
        //Demande du seuil
        Label l_seuil = new Label("Seuil : ");

        l_seuil.setLayoutX(25);
        l_seuil.setLayoutY(50);

        //SLIDER
        Slider slider = new Slider();
        slider.setMin(0);
        slider.setMax(255);
        slider.setValue(125);
        slider.setShowTickLabels(true);
        slider.setShowTickMarks(true);
        slider.setMajorTickUnit(50);
        slider.setMinorTickCount(15);
        slider.setBlockIncrement(5);

        slider.setLayoutX(25);
        slider.setLayoutY(120);
        slider.setPrefSize(200, 30);

        //LABEL AFFICHE SEUIL SELECTIONNE
        Label l_nbSeuil = new Label();
        l_nbSeuil.setText(""+slider.getValue());

        l_nbSeuil.setLayoutX(35);
        l_nbSeuil.setLayoutY(80);

        ///////////////////BOUTONS
        Button bt_seuillage = new Button("SEUILLAGE");
        Button bt_erosion = new Button("EROSION");
        Button bt_dilatation = new Button("DILATION");
        Button bt_ouverture = new Button("OUVERTURE");
        Button bt_fermeture = new Button("FERMETURE");

        //POSITION
        bt_erosion.setLayoutX(25);
        bt_erosion.setLayoutY(190);
        bt_erosion.setPrefSize(200,30);

        bt_dilatation.setLayoutX(25);
        bt_dilatation.setLayoutY(250);
        bt_dilatation.setPrefSize(200,30);

        bt_ouverture.setLayoutX(25);
        bt_ouverture.setLayoutY(320);
        bt_ouverture.setPrefSize(200,30);

        bt_fermeture.setLayoutX(25);
        bt_fermeture.setLayoutY(390);
        bt_fermeture.setPrefSize(200,30);


        //IMAGE
        Rectangle rect_image = new Rectangle() ;

        rect_image.setHeight(512);
        rect_image.setWidth(512);
        rect_image.setX(350);
        rect_image.setY(175);

        rect_image.setFill(Color.TRANSPARENT);
        rect_image.setStroke(Color.BLACK);

        final Button btn_ouvrir_image = new Button("Ouvrir une image");
        btn_ouvrir_image.setLayoutX(550);
        btn_ouvrir_image.setLayoutY(700);
        btn_ouvrir_image.setPrefSize(200,30);

        btn_ouvrir_image.setOnAction(actionEvent -> {
            final FileChooser dialog = new FileChooser();
            final File file = dialog.showOpenDialog(btn_ouvrir_image.getScene().getWindow());
            if (file != null) {
                URL url =  getClass().getResource(file.getPath());
                System.out.println("URL : "+ file.getPath());

                Image img = new Image(getClass().getResource("/images/"+file.getName()).toExternalForm());
                ImageView imageView = new ImageView(img);

                imageView.setFitWidth(512);
                imageView.setLayoutX(350);
                imageView.setLayoutY(175);
                imageView.setPreserveRatio(true);

                this.getChildren().add(imageView);

            }
        });


        //APPUIE SUR BOUTON
        bt_seuillage.setOnAction(new EventHandler<ActionEvent>(){
            @Override
            public void handle(ActionEvent event) {


            }
        });


        //AJOUTER A LA FENETRE
        this.getChildren().add(slider);
        this.getChildren().add(l_seuil);
        //this.getChildren().add(l_nbSeuil);
        this.getChildren().add(bt_erosion);
        this.getChildren().add(bt_dilatation);
        this.getChildren().add(bt_ouverture);
        this.getChildren().add(bt_fermeture);
        this.getChildren().add(rect_image);
        this.getChildren().add(btn_ouvrir_image);

    }


}
